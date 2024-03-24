# this runs server code for the python server

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from algorithm import containerizeOriginal
from dealerECOutput import determine_Remainder
from flask_cors import CORS
from parsingData import parseData
from openai import OpenAI
from nonSplitRecursive import nonSplit
import re
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

client = OpenAI(
    api_key=''
)

app = Flask(__name__)
api = Api(app)
CORS(app)

limiter = Limiter(
    app=app,
    key_func=get_remote_address,  # Use the remote address of the client as the key for rate limiting
    default_limits=["200 per hour"]  # Global rate limit
)

class Containerize(Resource):

    def generate_openai_completion(self, input_text):
        # From this table i want you to output an array in this format [[(EC number which is the 10th column),(QTY number which is the 12 column)], [x,x]...], where each EC number is listed in the first node of each sublist, and then the EC's respective QTY is listed in the second. Do not show the code process, i just want the output given to me after all the code is done. Disregard all other data other than the EC and the QTY columns so each sublist has only two items. Columns for data, 1: Model, 2: Order, 3: PO, 4: Dealer, 5: City, 6: State, 7: RDD, 8: TTE, Two blank columns you can disregard, 10: EC, 11: Order, 12: QTY, 13: WGT, 14: LD.EF. The data should not have parenthesis or any other types of extra characters, also it should be in this (example format): [[140,28], [192,16,], [204,2,], [636,29],...] In the case that multiple EC's are the same just combine them together and sum the quantities of the two
        # Define your additional instructions or context
       
        instruction = """
        From the dealer name of the shipment, match from the array below as to which one it is most similar or most likely to be assigned to. Just a note: AAFES is anything Army, Navy or military related. You can also use the City and State of the data to help determine which one it is.[
            "Costco US",
            "Costco Canada",
            "Best Buy",
            "Best Buy Canada",
            "Tech Data Canada",
            "Amazon US",
            "Amazon Canada",
            "Walmart US",
            "Walmart Canada",
            "Tech Data US",
            "AAFES",
            "London Drugs",
            "Sam's",
            "Target",
            "BJ's",
            "PC Richard",
            "ABT",
            "RC Willey",
            "New Age",
            "Interbond"
        ] If the dealer's name in the shipment data cannot be determined from the provided information return return zzzOthers- USzzzz. If there is a match return one of the simplified names above in the array and put zzz before the name and zzz after the name. For example zzzdealernamefromarrayzzz. 
        """

        # Combine the instruction with the input text
        combined_text = f"{input_text}\n\n{instruction}"

        # Generate a chat completion using the input text
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": combined_text}]
        )
        return chat_completion


    def split(self, pallets):

        return containerizeOriginal(pallets)

    def nonSplit(self, pallets):
        return nonSplit(pallets)


    @limiter.limit("10 per minute")
    def post(self):
        # Get the JSON data from the request
        data = request.get_json()

        # Ensure that the 'data' field is present in the JSON request
        if 'data' in data:


            parsed_strict_no_empty_after_dealer = []

            qtySum = 0
            lines = 0
            dealers = set()

            for line in data['data'].strip().split('\n'):

                lines += 1
                # Splitting by tab character
                columns = line.split('\t')

                # Remove any empty columns immediately following the dealer
                dealer_index = 3  # Assuming dealer is always in the 4th column
                while dealer_index + 1 < len(columns) and columns[dealer_index + 1].strip() == '':
                    columns.pop(dealer_index + 1)

                # Remove any empty columns after the 10th element
                while len(columns) > 10 and columns[10].strip() == '':
                    columns.pop(10)
                columns[12]
                qtySum += int(columns[12])

                # Add dealer name to the set
                dealers.add(columns[dealer_index])

                # Check if there are more than two unique dealers
                if len(dealers) > 2:
                    return {'error': 'More than two dealers please try again'}, 400
                
                parsed_strict_no_empty_after_dealer.append(columns)

            if qtySum > 3000:
                return {'error': 'QTY too high'}, 400
            elif lines > 70:
                return {'error': 'Too many lines, reduce the number of lines in your data'}, 400
            else:
                pass

            
            self.gpt = self.generate_openai_completion(data['data'])
            gptResponse = self.gpt.choices[0].message.content

            pattern = r'zzz(.+?)zzz'
            attempt = gptResponse
            match = re.search(pattern, attempt, re.DOTALL)

            if match:
                self.captured_content = match.group(1)
            else:
                self.captured_content = 'Other- US'

            def check_store(store):
                non_split_stores = ["Costco US", "Costco Canada", "AAFES", "BJ's", "London Drugs"]
                split_stores = ["Best Buy", "Best Buy Canada", "Tech Data Canada", "Amazon US", "Amazon Canada", 
                                "Walmart US", "Walmart Canada", "Tech Data US", "Sam's", "Target", "PC Richard", 
                                "ABT", "RC Willey", "New Age", "Interbond", "Other- US", "Others - Canada"]

                if store in non_split_stores:
                    self.method_number = 2
                    return "non split"
                elif store in split_stores:
                    self.method_number = 1
                    return "split"
                else:
                    self.method_number = 1
                    return "split"

            self.storage = check_store(self.captured_content)

            if not data['bestBuyCanOption']:
                pass
            else:

                self.captured_content = "Best Buy Canada"
                self.method_number = 1

            if data['splitOption'] == 'splitPallet':
                self.method_number = 1
                self.storage = "split"
            elif data['splitOption'] == 'dontSplitPallet':
                self.method_number = 2
                self.storage = "non split"
            else:
                pass


            if(self.captured_content == 'Best Buy Canada'):
                self.bestBuyCanada = True
            else:
                self.bestBuyCanada = False

            self.data = parseData(parsed_strict_no_empty_after_dealer, self.storage, self.bestBuyCanada)

            result = None

            if int(self.method_number) == 1:
                result = self.split(self.data[0])
            elif int(self.method_number) == 2:
                result = self.nonSplit(self.data[0])
            else:
                return {'error': 'Issue splitting pallet'}, 400

            # Return the results as JSON

            if len(result[0]) > 8:
                return {'error': 'More than 8 trailers returned. Please reduce QTY'}, 400

            dealerEC = determine_Remainder(self.data, result[1])

            qtySumOfResult = {key: sum(sub_array[2] for sub_array in value) for key, value in dealerEC.items()}
            totalSumOfResults = sum(sum(item[2] for item in value) for value in dealerEC.values())

            return jsonify(result, self.captured_content, self.method_number, dealerEC, qtySum, qtySumOfResult, totalSumOfResults)
        

        # If 'data' field is missing in the JSON request, return an error
        return jsonify({'error': 'Missing data field'}), 400

api.add_resource(Containerize, '/containerize')

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True, port=5000)