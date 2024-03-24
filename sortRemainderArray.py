# this is a function used in the algorithm that will sort the remainder data by the pallet length then the EC number so that 
# it will be able to containerize the remainders properly. You can't have pallet lengths lower regardless of the EC number
# the sort remainder algorithm needs to have structure in terms of where the EC's are placed due to how it iterates over the array

def sortRemainder(rmdata):

    ec_pallet_matrix = [
        (6, [18, 19, 36, 37, 48, 49]),
        (7, [84, 85, 87, 88, 112, 113, 126, 127, 140, 141, 168, 169]),
        (8, [160, 161, 170, 171, 176, 177, 186, 187, 188, 189, 192, 193, 204, 205, 222, 223]),
        (9, [190, 191, 216, 217, 224, 225, 228, 229, 246, 247, 248, 249, 252, 253]),
        (10, [200, 201, 240, 241, 260, 261, 280, 281, 360, 361, 375, 376, 378, 379]),
        (11, [264, 265, 308, 309, 396, 397, 408, 409, 411, 412, 414, 415, 429, 430, 444, 445, 447, 448, 462, 463, 480, 481, 483, 484, 495, 496, 510, 511, 513, 514]),
        (12, [288, 289, 384, 385, 432, 433, 576, 577, 597, 598, 600, 601, 633, 634, 636, 637]),
        (13, [468, 469, 507, 508, 546, 547, 585, 586, 624, 625, 663, 664]),
        (14, [336, 337, 448, 449, 588, 589, 630, 631, 672, 673, 708, 709, 750, 751, 900, 901, 960, 961, 1020, 1021, 1024, 1025]),
        (18, [1216, 1217, 1425, 1426, 1520, 1521])
    ]

    # Function to map EC numbers to pallet lengths
    def map_ec_to_pallet_length(ec_pallet_matrix):
        ec_pallet_map = {}
        for length, ec_numbers in ec_pallet_matrix:
            for ec in ec_numbers:
                ec_pallet_map[ec] = length
        return ec_pallet_map

    # Function to sort new data based on pallet length from the matrix
    def advanced_custom_sort_with_new_data(new_data, ec_pallet_map):
        # Extract EC numbers from the new data for sorting
        ec_numbers = [item[0] for item in new_data]

        # Sort the EC numbers primarily based on pallet length, then by EC number
        sorted_ec_numbers = sorted(ec_numbers, key=lambda x: (ec_pallet_map.get(x, float('inf')), x))

        # Return the sorted list along with their corresponding pallet lengths from the matrix
        return [(ec_pallet_map.get(ec, None), ec) for ec in sorted_ec_numbers]

    # Example new data to sort
    new_data = rmdata

    # Create the EC number to pallet length mapping
    ec_pallet_map = map_ec_to_pallet_length(ec_pallet_matrix)

    # Sort the new data
    sorted_advanced_with_new_data = advanced_custom_sort_with_new_data(new_data, ec_pallet_map)
    
    sort_order = [item[1] for item in sorted_advanced_with_new_data]

    # Creating a mapping of the first item in each sub-array to its position in the sort order
    position_map = {value: index for index, value in enumerate(sort_order)}

    # Sorting the array based on the position map
    sorted_array_correct = sorted(new_data, key=lambda x: position_map.get(x[0]))
    return sorted_array_correct