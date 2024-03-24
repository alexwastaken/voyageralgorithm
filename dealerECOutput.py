# this is a function that helps the server return the EC's per dealer and per trailer so it can be shown on the main site

import functions
def determine_Remainder(sampleData, result):

    def consolidate_data_by_trailer_and_ec(data):
        # Dictionary to hold the consolidated data
        consolidated = {}

        # Iterate through each entry in the data
        for entry in data:
            ec_number, quantity, trailer_number, category, unknown_value = entry

            # Creating a unique key for each combination of EC number and trailer number
            key = (ec_number, trailer_number)

            # Check if the key exists in the dictionary
            if key in consolidated:
                # Update the quantity for the existing key
                consolidated[key][1] += quantity
            else:
                # Create a new entry for the key
                consolidated[key] = [ec_number, quantity, trailer_number, category, unknown_value]

        # Convert the dictionary back to the list format
        consolidated_list = list(consolidated.values())

        return consolidated_list

    consolidated_data_by_trailer_and_ec = consolidate_data_by_trailer_and_ec(result)

    dealerEC = {}

    for g in consolidated_data_by_trailer_and_ec:

        incremented_EC_Number = 0

        if(functions.ecIncrementedCheck(g[0]) and sampleData[1][1]):

            dealer_name = sampleData[1][1]
            incremented_EC_Number = 1
            
        else:

            dealer_name = sampleData[1][0]
        
        adjusted_ec_number = g[0] - 1 if incremented_EC_Number == 1 else g[0]

        if g[2] not in dealerEC:
            dealerEC[g[2]] = [[dealer_name, adjusted_ec_number, g[1], incremented_EC_Number]]
        else:
            dealerEC[g[2]].append([dealer_name, adjusted_ec_number, g[1], incremented_EC_Number])

    return dealerEC