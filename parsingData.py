# this function will take in the ECQTYDATA and it will identify if it should be split or non split, if its split it will consolidate the data, if non split it will
# not consolidate thee data, it will also increment the EC number by 1 if it has multiple dealers

def parseData(ecQTYData, splitornosplit, bestBuyCanada):

    def parse_and_modify_data(data):
        modified_data = []
        
        for item in data:
            # Extract the first element (model number)
            model_number = item[0]

            # Find the first occurrence of a digit in the model number
            for i, char in enumerate(model_number):
                if char.isdigit():
                    break
            
            # Extract the two-digit number
            two_digit_number = int(model_number[i:i+2])

            # Check if the number is less than 60 and modify the 4th element
            if two_digit_number < 60:
                item[3] += " <55"
            elif two_digit_number > 60:
                item[3] += " >65"
            else:
                pass

            modified_data.append(item)
        
        return modified_data
    
    if(bestBuyCanada):
        ecQTYData = parse_and_modify_data(ecQTYData)
    else:
        pass

    subArrays = {}
    dealers = {}

    for item in ecQTYData:
        dealer_name = item[3]
        if dealer_name not in dealers:
            dealers[dealer_name] = len(dealers)
            subArrays[dealer_name] = []

        subArrays[dealer_name].append([item[10], item[12]])

    if splitornosplit == "split":
        # Function to consolidate quantities
        def consolidate_quantities(items):
            consolidated = {}
            for item_code, quantity in items:
                if item_code in consolidated:
                    consolidated[item_code] += int(quantity)
                else:
                    consolidated[item_code] = int(quantity)
            return [[item_code, str(consolidated[item_code])] for item_code in consolidated]

        # Consolidating data for each dealer
        consolidated_data = {dealer: consolidate_quantities(items) for dealer, items in subArrays.items()}
    else:
        # Skip consolidation if not split
        consolidated_data = subArrays

    dealer_names = list(dealers.keys())

    if len(dealer_names) >= 2:
        # Extract item codes from the first dealer
        first_dealer_items = {item[0] for item in consolidated_data[dealer_names[0]]}

        if len(dealer_names) >= 2:
            # Increment the item code by 1 in the second dealer for all items
            for i, item in enumerate(consolidated_data[dealer_names[1]]):
                consolidated_data[dealer_names[1]][i][0] = str(int(item[0]) + 1)

    combined_items = []
    for dealer in dealer_names:
        for item in consolidated_data[dealer]:
            # Convert string quantities to integers for consistency
            combined_items.append([int(item[0]), int(item[1])])


    return [combined_items, dealer_names]
