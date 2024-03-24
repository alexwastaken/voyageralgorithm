# this recursively runs through each sublist in the array running the algorithm function for each sublist and if it creates more than one
# pallet array it will containerize that and post it, then it will continue on with the next ec number

from algorithm import containerizeOriginal
import copy

def nonSplit(data):

    sorted_zzz = sorted(data, key=lambda x: x[0] / x[1], reverse=True)
    nextList = []

    for i in range(len(sorted_zzz)):
        # Create a new list for each sublist and append it to nextList
        sublist = [sorted_zzz[:i + 1]]
        nextList.extend(sublist)

    shipment = []
    start = 0
    shipmentNumber = 0
    
    for index, item in enumerate(nextList):

        checker = containerizeOriginal(item[start:])

        if (len(checker[0]) - 1) > 0:

            first = copy.deepcopy(containerizeOriginal(item[start:index]))
            # print(first, item_copy, '==============')

            second = copy.deepcopy(containerizeOriginal([item[index]]))
            first_element_list = first[0][0]
            second_element_sublists = [sublist for sublist in first[1] if sublist[2] == 0]
            third_element_first_item = first[2][0]

            # this is if it is a perfect pallet and the only perfect pallet sometimes it returns 1 as the only pallet array so i have to capture that if its the case

            second_element_list = second[0][0]
            second_element_sublists_second_shipment = [sublist for sublist in second[1] if sublist[2] == 0]
            third_element_second_item_ = second[2][0]
           
            for sublist in second_element_sublists:
                sublist[2] = shipmentNumber
            shipmentNumber += 1

            shipment.append([first_element_list, second_element_sublists, third_element_first_item])
    
            if(index == len(nextList) - 1):

                for sublist in second_element_sublists_second_shipment:
                    sublist[2] = shipmentNumber
                shipmentNumber += 1
                shipment.append([second_element_list, second_element_sublists_second_shipment, third_element_second_item_])

            start = index

        elif(index == len(nextList) - 1):

            third = containerizeOriginal(item[start:])

            endFirst = next(iter(third[0].values()))
            endSecond = [sublist for sublist in third[1]]
            endThird = third[2]
            # print([endFirst, endSecond, endThird])
            for sublist in endSecond:
                sublist[2] = shipmentNumber
            shipmentNumber += 1
            shipment.append([endFirst, endSecond, endThird])
            break
            # this is setting start to item because you want to just start the next one after the current item that was added
            # this used to be start = len(item - 1)
    def convertData(zzz):
        # Initialize a dictionary for the first elements
        first_elements_dict = {}
        combined_second_elements = []
        third_elements = []

        for i, entry in enumerate(zzz):
            # Assign the entire first sublist to the dictionary under its index
            first_elements_dict[i] = entry[0]

        # Combining the second elements
        for entry in zzz:
            combined_second_elements.extend(entry[1])

        # Appending the third elements
        third_elements = [entry[2] for entry in zzz]

        # Creating the final structure
        final_structure = [first_elements_dict, combined_second_elements, third_elements]

        return final_structure
    return convertData(shipment)