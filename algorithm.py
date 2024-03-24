# this is the main algorithm

import math
import functions
import copy
from sortRemainderArray import sortRemainder

def containerizeOriginal(sampleData):

	algorithmData = copy.deepcopy(sampleData)
	
	# the code block below determines perfect pallet QTYS's
	perfectPallets = []

	for i, blah in enumerate(algorithmData):

		checker = functions.ecIncrementedCheck(blah[0])

		if not checker:
			if blah[1] > blah[0]:

				perfectPallets.append([blah[0], blah[0]])

				algorithmData[i][1] = blah[1] - blah[0]
			elif blah[1] == blah[0]:
				
				perfectPallets.append([blah[1], blah[1]])

				algorithmData[i][1] = 0

		else:
			blah[0] -= 1
			if blah[1] > blah[0]:

				perfectPallets.append([blah[0] + 1, blah[0]])
				
				algorithmData[i][1] = blah[1] - blah[0]
			elif blah[1] == blah[0]:
				perfectPallets.append([blah[0] + 1, blah[0]])

				algorithmData[i][1] = 0
			blah[0] += 1

	d = []
	# d is for double pallets
	s = []
	# s is for single pallets
	r = []
	# r is for remainders for the first dealer
	r2 = []
	# r2 is for remainders for the second dealer

	# this is a function that loops through simpleData which contains the raw data EC number and QTY.
	for item in algorithmData:
		# this will calculate the number of double pallets
		double = functions.findPallet(2, item[0]) * math.floor(functions.divide(item[1], functions.findPallet(2, item[0])))
		
		# only append if double is not 0
		if double != 0:
			for i in range(math.floor(functions.divide(item[1], functions.findPallet(2, item[0])))):
				d.append([item[0], functions.findPallet(2, item[0]), functions.gen(), 'D'])

		# this will calculate the number of single pallets
		
		single = functions.findPallet(1, item[0]) * math.floor(functions.divide(item[1] - double, functions.findPallet(1, item[0])))
		if(single > functions.findPallet(1, item[0])):
			numberOfSingles = int(single / functions.findPallet(1, item[0]))

			for z in range(numberOfSingles):
				s.append([item[0], functions.findPallet(1, item[0]), functions.gen(), 'S'])
			
		elif single != 0:

			s.append([item[0], single, functions.gen(), 'S'])
		
		# this will calculate the number of remainder units
		remainder = item[1] - (double + single)
		if(remainder == 0):
			pass
		else:
			if(functions.remainderType(item[0])):
				if functions.ecIncrementedCheck(item[0]):
					
					r2.append([item[0], remainder, functions.gen(), 'R'])
				else:
					r.append([item[0], remainder, functions.gen(), 'R'])
			else:
				pass
	# array stores EC of remainder pallet being made, how much left is needed for single pallet, single pallet is at half capacity, id of remainder pallet

	# the remainderArray2 array contains the remainder pallets were built
			
	remainderArray2 = []

	# the builderarray is an array used to store the main building blocks of the shipments, and for the remainders it will store just the pallet that the biggest remainder is on and the remainderarray2 will go into more detail on each of the pallets

	builderArray = []

	for f in d:
		builderArray.append([f[0], f[1], f[2], 'D', functions.testCLE(f[0], 'd')])

	for f in s:

		builderArray.append([f[0], f[1], f[2], 'S', functions.testCLE(f[0], 's')])


	# this for loop loops through each line and will build basic pallets. This function builds remainder pallets
	def remainder_insert(array, dealer):

		if(dealer == 1):
			dealer_1_remainders = r
		else:
			dealer_1_remainders = r2

		testing = sortRemainder(array)


		palletEC = 0
		palletQTY = 0
		palletID = functions.gen()

		# this array holds the remainders like 468 that need to have another chance to build
		# this function that will take in the EC number and the QTY and return to you how much is needed for single pallet and if it is currently at 50% of a half pallet, if it is above half a pallet omit the second part

		def remaining():

			ECQuantity = functions.findPallet(1,palletEC)
			needed = ECQuantity - palletQTY

			if needed == (ECQuantity / 2):
				return [needed, True]
			elif needed < 0:
				return [0, False]
			else:	
				return [needed, False]

		for index, item in enumerate(testing):

			if(item[1] == 0):
				continue

			if(palletQTY == 0):
				palletEC = item[0]

			if palletEC > item[0]:

				remainder_insert(testing[index:], dealer_1_remainders)
				continue

			r1 = remaining()

			if r1[1]:

				tripleStack = [360, 375, 378, 396, 408, 411, 414, 429, 432, 444, 447, 462, 468, 480, 483,
				495, 507, 510, 513, 546, 576, 585, 588, 597, 600, 624, 630, 633, 636, 663,
				672, 708, 750, 900, 960, 1020, 1024, 1216, 1425, 1520]
				
				if item[0] in tripleStack:
					totalNeeded = int(functions.findPallet(1,item[0]) / 3)
				else:
					totalNeeded = int(functions.findPallet(1,item[0]) / 2)

				if item[1] >= totalNeeded:

					palletQTY += totalNeeded

					item[1] = item[1] - totalNeeded

					if(index == len(testing) - 1 and totalNeeded > 0):

						remainderArray2.append([item[0], totalNeeded, palletID, 'R', palletID])
						continue
					
					remainderArray2.append([item[0], totalNeeded, item[2], 'R', palletID])

					palletQTY = item[1]
					palletID = functions.gen()

					if(item[1] > 0):
						remainderArray2.append([item[0], item[1], item[2], 'R', palletID])
						item[1] = 0
						palletEC = item[0]
					else:
						pass

				else:
					if index == len(dealer_1_remainders) - 1:
						pass
					palletQTY += item[1]

					remainderArray2.append([item[0], item[1], item[2], 'R', palletID])
					item[1] = 0
					
			else:

				if r1[0] > item[1]:

					palletQTY += item[1]

					remainderArray2.append([item[0], item[1], item[2], 'R', palletID])

					item[1] = 0
				
				elif r1[0] < item[1]:

					palletQTY += r1[0]

					item[1] = item[1] - r1[0]

					if(index == len(testing) - 1 and item[1] - r1[0] > 0):
						
						remainderArray2.append([item[0], r1[0], item[2], 'R', palletID])
						palletID = functions.gen()
						remainderArray2.append([item[0], item[1], item[2], 'R', palletID])
						item[1] = 0
						continue

					if(r1[0] == 0):
						pass
					else:

						remainderArray2.append([item[0], r1[0], item[2], 'R', palletID])

					palletQTY = item[1]
					palletID = functions.gen()


					if(item[1] > 0):

						remainderArray2.append([item[0], item[1], item[2], 'R', palletID])
						item[1] = 0
						palletEC = item[0]
					else:
						pass


				elif r1[0] == item[1]:
	
					palletQTY += r1[0]

					remainderArray2.append([item[0], r1[0], item[2], 'R', palletID])
					palletQTY = 0
					palletID = functions.gen()
					item[1] = 0

				elif r1[0] == 0:
					pass

			if(index == len(testing) - 1 and item[1] > 0):
				
				remainderArray2.append([item[0], item[1], item[2], 'R', palletID])


	# this will run the function on both dealers if needed and it will append the remainder pallets to remainderarray2
	remainder_insert(r, 1)
	remainder_insert(r2, 2)


	# this will take all the entries in the remainderArray2 and take the first instance of the id and append it to builderarray
	# Sort the array based on the first item of each sub-array
	sorted_data = sorted(remainderArray2, key=lambda x: x[0])
	seen_fourth_items = set()

	for item in sorted_data:
		fourth_item = item[4]
		if fourth_item not in seen_fourth_items:
			# Append new entry to builderArray
			new_entry = [
				item[0],
				functions.findPallet(1, item[0]),
				item[4],
				'R',
				functions.testCLE(item[0], 's')
			]
			builderArray.append(new_entry)
			seen_fourth_items.add(fourth_item)

	# write a function that will use the two below arrays to return the EC and the QTY + consolidate the EC and QTY per container EC while returning the correct pallet level for the remainders

	def findTotalCLE(checkArray, shipmentNumber):

		cle = 0
		for x in checkArray:
			if x[1] == shipmentNumber:
				cle += x[0][4]
		return cle

	shipments = []
	totalShipments = 0


	# this will append all the items in builderArray to trailers and will only hit 100% the new array is called shipments and contains information based on which trailer these units are going to

	for i in builderArray:

		if i[3] == 'D':
			
			if(findTotalCLE(shipments, totalShipments) + i[4] <= 1.000000002):

				shipments.append([i, totalShipments])
			else:
				totalShipments += 1
				shipments.append([i, totalShipments])
		elif i[3] == 'S':
			# Attempt to find a shipment where the 'S' pallet can fit
			shipmentAdded = False
			for z in range(totalShipments + 1):
				if findTotalCLE(shipments, z) + i[4] <= 1.000000002:

					shipments.append([i, z])
					shipmentAdded = True
					break
			
			# If the pallet didn't fit in any existing shipment, create a new one
			if not shipmentAdded:
				totalShipments += 1
				shipments.append([i, totalShipments])

		elif i[3] == 'R':
			
			shipmentAdded = False
			for z in range(totalShipments + 1):

				if findTotalCLE(shipments, z) + i[4] <= 1.000000002:
					shipments.append([i, z])
					shipmentAdded = True
					break

			# If the pallet didn't fit in any existing shipment, create a new one
			if not shipmentAdded:

				totalShipments += 1
				shipments.append([i, totalShipments])
	# below perfect pallets are added as well to shipments
	for z in perfectPallets:

		if(len(shipments) == 0):
			totalShipments = 0
		else:
			totalShipments += 1
		shipments.append([[z[0], z[1], functions.gen(), 'F', 1], totalShipments])

	containerized = []
	# the final type of array is called containerized which is used below to send out the last bits of data of the algorithm
	# below are all the final functions that are used to build the final trailer report not much math more or less just consolidation etc
	for z in shipments:

		if z[0][3] == 'F':
			containerized.append([z[0][0], z[0][1], z[1], z[0][3], functions.find_key_by_value(z[0][0])])

		if z[0][3] == 'D' or z[0][3] == 'S':

			containerized.append([z[0][0], z[0][1], z[1], z[0][3], functions.find_key_by_value(z[0][0])])

		elif z[0][3] == 'R':

			# Create a dictionary to map palletID to its items
			pallet_dict = {}
			for x in remainderArray2:
				palletID = x[4]
				if palletID not in pallet_dict:
					pallet_dict[palletID] = []

				pallet_dict[palletID].append(x)
			# Check if the current shipment's palletID is in the dictionary
			palletID = z[0][2]
			if palletID in pallet_dict:
				for b in pallet_dict[palletID]:

					position = 0
					for t in builderArray:
						if b[4] == t[2]:
				
							position = functions.find_key_by_value(t[0])
							break  # Break as soon as the match is found
					
					containerized.append([b[0], b[1], z[1], z[0][3], position])
		else:
			pass


	def count_pallets_dynamic(pallets):

		# Initialize a dynamic dictionary to keep track of shipment counts
		shipment_counts = {}

		for item in shipments:

			# im adding this so i can make sure that for perfect pallets it has a 0 instead of 1 when it returns


			sublist = item[0]
			ec_number, _, shipment, type_ = sublist[0], sublist[1], item[1], sublist[3]

			# Initialize the shipment count array if it doesn't exist for this shipment
			if shipment not in shipment_counts:
				shipment_counts[shipment] = [0] * 10

			# Find the pallet index for the given EC number
			for pallet_index, ec_numbers in pallets.items():
				
				if ec_number in ec_numbers:
				# Increment the pallet count based on type 'D', 'S', 'R', or 'F'
					if type_ in ['D', 'S', 'R', 'F']:
						if type_ == 'D':
							increment = 2
						elif type_ == 'S' or type_ == 'R':
							increment = 1
						else:
							increment = functions.fullPalletSearch(ec_number)
					else:
						increment = 1
					shipment_counts[shipment][pallet_index] += increment
					break
		return shipment_counts
	
	def consolidate_shipments(data):
	
		# Initialize dictionaries to store consolidated data and non-consolidated data
		consolidated = {}
		non_consolidated = []

		for ec_number, qty, shipment_id, type, palletPosition in data:
			# Handle 'D' type for consolidation
			if type == 'D':
				# Create a unique key for each EC number and shipment ID
				key = (ec_number, shipment_id)
				# Add the quantity to the existing quantity or set it if it's the first time
				if key in consolidated:
					consolidated[key] += qty
				else:
					consolidated[key] = qty
			else:
				# For 'S' and 'R', just add them to the non-consolidated list
				non_consolidated.append([ec_number, qty, shipment_id, type, palletPosition])

		# Convert consolidated data back to the original format
		consolidated_list = [[ec, qty, shipment_id, 'D', functions.find_key_by_value(ec)] for (ec, shipment_id), qty in consolidated.items()]

		# Combine the consolidated and non-consolidated lists
		result = consolidated_list + non_consolidated


		return result

	allConsolidatedShipments = consolidate_shipments(containerized)
	
	CLEofTrailers = []

	for q in count_pallets_dynamic(functions.pallets).values():

		
		CLEofTrailers.append(functions.trailerCLE(q))

	return [count_pallets_dynamic(functions.pallets), allConsolidatedShipments, CLEofTrailers]
