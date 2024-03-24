# these are all functions that relate to searching and calulating trailer CLE used in the algorithm function

import random

def gen(length=32):
    # The ID will be a random number with 'length' digits
    range_start = 10**(length-1)
    range_end = (10**length)-1
    return str(random.randint(range_start, range_end))

def divide(dividend, divisor):
    try:
        return dividend/divisor
    except ZeroDivisionError:
        return 0
    
def trailerCLE(palletArray):

    ec_36_totalpallet = 12
    ec_84_87_112_totalpallet = 14
    ec_186_188_192_204_totalpallet = 16
    ec_216_228_246_totalpallet = 18
    ec_240_260_totalpallet = 20
    ec_308_429_444_463_495_510_513_totalpallet = 22
    ec_633_636_totalpallet = 24
    ec_468_507_663_totalpallet = 26
    ec_672_750_totalpallet = 28
    ec_1140_1450_totalpallet = 38

    ec_36_fillpercentage = divide(palletArray[0],ec_36_totalpallet)
    ec_84_87_112_fillpercentage = divide(palletArray[1],ec_84_87_112_totalpallet)
    ec_186_188_192_204_fillpercentage = divide(palletArray[2],ec_186_188_192_204_totalpallet)
    ec_216_228_246_fillpercentage = divide(palletArray[3],ec_216_228_246_totalpallet)
    ec_240_260_fillpercentage = divide(palletArray[4],ec_240_260_totalpallet)
    ec_308_429_444_463_495_510_513_fillpercentage = divide(palletArray[5],ec_308_429_444_463_495_510_513_totalpallet)
    ec_633_636_fillpercentage = divide(palletArray[6],ec_633_636_totalpallet)
    ec_468_507_663_fillpercentage = divide(palletArray[7],ec_468_507_663_totalpallet)
    ec_672_750_fillpercentage = divide(palletArray[8],ec_672_750_totalpallet)
    ec_1140_1450_fillpercentage = divide(palletArray[9],ec_1140_1450_totalpallet)


    totalfillpercentage = ec_36_fillpercentage + ec_84_87_112_fillpercentage + ec_186_188_192_204_fillpercentage + ec_216_228_246_fillpercentage + ec_240_260_fillpercentage + ec_308_429_444_463_495_510_513_fillpercentage + ec_633_636_fillpercentage + ec_468_507_663_fillpercentage  + ec_672_750_fillpercentage + ec_1140_1450_fillpercentage

    return totalfillpercentage

def ecIncrementedCheck(Ectocheck):
    ecIncremented = [19, 37, 49, 85, 88, 113, 127, 141, 161, 169, 171, 177, 187, 189, 191, 193, 201, 205, 217, 223, 225, 229, 241, 247, 249, 253, 261, 265, 281, 289, 309, 337, 361, 376, 379, 385, 397, 409, 412, 415, 430, 433, 445, 448, 449, 463, 469, 481, 484, 496, 508, 511, 514, 547, 577, 586, 589, 598, 601, 625, 631, 634, 637, 664, 673, 709, 751, 901, 961, 1021, 1025, 1217, 1426, 1521]
    for x in ecIncremented:
        if x == Ectocheck:
            return True
    return False

def testCLE(ec_number, pallet_type):
    ec_totalpallet = [
        (18, 12), (19, 12), (36, 12), (37, 12), (48, 12), (49, 12), 
        (84, 14), (85, 14), (87, 14), (88, 14), (112, 14), (113, 14), 
        (126, 14), (127, 14), (140, 14), (141, 14), (168, 14), (169, 14), 
        (160, 16), (161, 16), (170, 16), (171, 16), (176, 16), (177, 16), 
        (186, 16), (187, 16), (188, 16), (189, 16), (192, 16), (193, 16), 
        (204, 16), (205, 16), (222, 16), (223, 16), (190, 18), (191, 18), 
        (216, 18), (217, 18), (224, 18), (225, 18), (228, 18), (229, 18), 
        (246, 18), (247, 18), (248, 18), (249, 18), (252, 18), (253, 18), 
        (200, 20), (201, 20), (240, 20), (241, 20), (260, 20), (261, 20), 
        (280, 20), (281, 20), (360, 20), (361, 20), (375, 20), (376, 20), 
        (378, 20), (379, 20), (264, 22), (265, 22), (308, 22), (309, 22), 
        (396, 22), (397, 22), (408, 22), (409, 22), (411, 22), (412, 22), 
        (414, 22), (415, 22), (429, 22), (430, 22), (444, 22), (445, 22), 
        (447, 22), (448, 22), (462, 22), (463, 22), (480, 22), (481, 22), 
        (483, 22), (484, 22), (495, 22), (496, 22), (510, 22), (511, 22), 
        (513, 22), (514, 22), (288, 24), (289, 24), (384, 24), (385, 24), 
        (432, 24), (433, 24), (576, 24), (577, 24), (597, 24), (598, 24), 
        (600, 24), (601, 24), (633, 24), (634, 24), (636, 24), (637, 24), 
        (468, 26), (469, 26), (507, 26), (508, 26), (546, 26), (547, 26), 
        (585, 26), (586, 26), (624, 26), (625, 26), (663, 26), (664, 26), 
        (336, 28), (337, 28), (448, 28), (449, 28), (588, 28), (589, 28), 
        (672, 28), (673, 28), (708, 28), (709, 28), (750, 28), (751, 28), 
        (630, 30), (631, 30), (900, 30), (901, 30), (960, 30), (961, 30), 
        (1020, 30), (1021, 30), (1024, 32), (1025, 32), (1216, 38), (1217, 38), 
        (1425, 38), (1426, 38), (1520, 38), (1521, 38)
    ]

    # Convert the pallet type from "s" or "d" to a number of pallets.
    pallets = 2 if pallet_type == "d" else 1

    # Find the total pallets for the given EC number
    total_pallets = None
    for ec, total in ec_totalpallet:
        if ec == ec_number:
            total_pallets = total
            break
    
    if total_pallets is None:
        raise ValueError(f"EC number {ec_number} not found in the list")

    # Calculate the CLE as the number of pallets divided by the total pallets for the EC number.
    cle = pallets / total_pallets

    # Return the calculated CLE
    return cle

def fullPalletSearch(ec):
    pallets = [
        (18, 12), (19, 12), (36, 12), (37, 12), (48, 12), (49, 12), 
        (84, 14), (85, 14), (87, 14), (88, 14), (112, 14), (113, 14), 
        (126, 14), (127, 14), (140, 14), (141, 14), (168, 14), (169, 14), 
        (160, 16), (161, 16), (170, 16), (171, 16), (176, 16), (177, 16), 
        (186, 16), (187, 16), (188, 16), (189, 16), (192, 16), (193, 16), 
        (204, 16), (205, 16), (222, 16), (223, 16), (190, 18), (191, 18), 
        (216, 18), (217, 18), (224, 18), (225, 18), (228, 18), (229, 18), 
        (246, 18), (247, 18), (248, 18), (249, 18), (252, 18), (253, 18), 
        (200, 20), (201, 20), (240, 20), (241, 20), (260, 20), (261, 20), 
        (280, 20), (281, 20), (360, 20), (361, 20), (375, 20), (376, 20), 
        (378, 20), (379, 20), (264, 22), (265, 22), (308, 22), (309, 22), 
        (396, 22), (397, 22), (408, 22), (409, 22), (411, 22), (412, 22), 
        (414, 22), (415, 22), (429, 22), (430, 22), (444, 22), (445, 22), 
        (447, 22), (448, 22), (462, 22), (463, 22), (480, 22), (481, 22), 
        (483, 22), (484, 22), (495, 22), (496, 22), (510, 22), (511, 22), 
        (513, 22), (514, 22), (288, 24), (289, 24), (384, 24), (385, 24), 
        (432, 24), (433, 24), (576, 24), (577, 24), (597, 24), (598, 24), 
        (600, 24), (601, 24), (633, 24), (634, 24), (636, 24), (637, 24), 
        (468, 26), (469, 26), (507, 26), (508, 26), (546, 26), (547, 26), 
        (585, 26), (586, 26), (624, 26), (625, 26), (663, 26), (664, 26), 
        (336, 28), (337, 28), (448, 28), (449, 28), (588, 28), (589, 28), 
        (672, 28), (673, 28), (708, 28), (709, 28), (750, 28), (751, 28), 
        (630, 30), (631, 30), (900, 30), (901, 30), (960, 30), (961, 30), 
        (1020, 30), (1021, 30), (1024, 32), (1025, 32), (1216, 38), (1217, 38), 
        (1425, 38), (1426, 38), (1520, 38), (1521, 38)
    ]

    for x in pallets:
        if x[0] == ec:
            return x[1]
        
def remainderType(ec_number):
    ec_totalpallet = [
        (18, 1), (19, 2), (36, 1), (37, 2), (48, 1), (49, 2), 
        (84, 1), (85, 2), (87, 1), (88, 2), (112, 1), (113, 2), 
        (126, 1), (127, 2), (140, 1), (141, 2), (168, 1), (169, 2), 
        (160, 1), (161, 2), (170, 1), (171, 2), (176, 1), (177, 2), 
        (186, 1), (187, 2), (188, 1), (189, 2), (192, 1), (193, 2), 
        (204, 1), (205, 2), (222, 1), (223, 2), (190, 1), (191, 2), 
        (216, 1), (217, 2), (224, 1), (225, 2), (228, 1), (229, 2), 
        (246, 1), (247, 2), (248, 1), (249, 2), (252, 1), (253, 2), 
        (200, 1), (201, 2), (240, 1), (241, 2), (260, 1), (261, 2), 
        (280, 1), (281, 2), (360, 1), (361, 2), (375, 1), (376, 2), 
        (378, 1), (379, 2), (264, 1), (265, 2), (308, 1), (309, 2), 
        (396, 1), (397, 2), (408, 1), (409, 2), (411, 1), (412, 2), 
        (414, 1), (415, 2), (429, 1), (430, 2), (444, 1), (445, 2), 
        (447, 1), (448, 2), (462, 1), (463, 2), (480, 1), (481, 2), 
        (483, 1), (484, 2), (495, 1), (496, 2), (510, 1), (511, 2), 
        (513, 1), (514, 2), (288, 1), (289, 2), (384, 1), (385, 2), 
        (432, 1), (433, 2), (576, 1), (577, 2), (597, 1), (598, 2), 
        (600, 1), (601, 2), (633, 1), (634, 2), (636, 1), (637, 2), 
        (468, 1), (469, 2), (507, 1), (508, 2), (546, 1), (547, 2), 
        (585, 1), (586, 2), (624, 1), (625, 2), (663, 1), (664, 2), 
        (336, 1), (337, 2), (448, 1), (449, 2), (588, 1), (589, 2), 
        (672, 1), (673, 2), (708, 1), (709, 2), (750, 1), (751, 2), 
        (630, 1), (631, 2), (900, 1), (901, 2), (960, 1), (961, 2), 
        (1020, 1), (1021, 2), (1024, 1), (1025, 2), (1216, 1), (1217, 2), 
        (1425, 1), (1426, 2), (1520, 1), (1521, 2)
    ]

    for pair in ec_totalpallet:
        if ec_number in pair:
            return True

    return False



def findPallet(palletID, ec):
    singlePallet = [
        [18, 1], [19, 1], [36, 3], [37, 3], [48, 4], [49, 4], [84, 6], [85, 6],
        [87, 6], [88, 6], [112, 8], [113, 8], [126, 8], [127, 8], [140, 10], [141, 10],
        [160, 10], [161, 10], [168, 12], [169, 12], [170, 10], [171, 10], [176, 10],
        [177, 10], [186, 10], [187, 10], [188, 10], [189, 10], [190, 10], [191, 10],
        [192, 12], [193, 12], [200, 10], [201, 10], [204, 12], [205, 12], [216, 12],
        [217, 12], [222, 12], [223, 12], [224, 12], [225, 12], [228, 12], [229, 12],
        [240, 12], [241, 12], [246, 12], [247, 12], [248, 12], [249, 12], [252, 14],
        [253, 14], [260, 12], [261, 12], [264, 12], [265, 12], [280, 14], [281, 14],
        [288, 12], [289, 12], [308, 14], [309, 14], [336, 12], [337, 12], [360, 18],
        [361, 18], [375, 18], [376, 18], [378, 18], [379, 18], [384, 16], [385, 16],
        [396, 18], [397, 18], [408, 18], [409, 18], [411, 18], [412, 18], [414, 18],
        [415, 18], [429, 18], [430, 18], [432, 18], [433, 18], [444, 18], [445, 18],
        [447, 18], [448, 18], [449, 16], [462, 21], [463, 21], [468, 18], [469, 18],
        [480, 21], [481, 21], [483, 21], [484, 21], [495, 21], [496, 21], [507, 18],
        [508, 18], [510, 21], [511, 21], [513, 21], [514, 21], [546, 21], [547, 21],
        [576, 24], [577, 24], [585, 21], [586, 21], [588, 21], [589, 21], [597, 24],
        [598, 24], [600, 24], [601, 24], [624, 24], [625, 24], [630, 21], [631, 21],
        [633, 24], [634, 24], [636, 24], [637, 24], [663, 24], [664, 24], [672, 24],
        [673, 24], [708, 24], [709, 24], [750, 24], [751, 24], [900, 28], [901, 28],
        [960, 32], [961, 32], [1020, 32], [1021, 32], [1024, 32], [1025, 32], [1216, 32],
        [1217, 32], [1425, 35], [1426, 35], [1520, 40], [1521, 40]
    ]
    doublePallet = [
        [18, 3], [19, 3], [36, 6], [37, 6], [48, 8], [49, 8], [84, 12], [85, 12],
        [87, 12], [88, 12], [112, 16], [113, 16], [126, 18], [127, 18], [140, 20],
        [141, 20], [160, 20], [161, 20], [168, 24], [169, 24], [170, 20], [171, 20],
        [176, 22], [177, 22], [186, 22], [187, 22], [188, 22], [189, 22], [190, 20],
        [191, 20], [192, 24], [193, 24], [200, 20], [201, 20], [204, 24], [205, 24],
        [216, 24], [217, 24], [222, 26], [223, 26], [224, 24], [225, 24], [228, 24],
        [229, 24], [240, 24], [241, 24], [246, 26], [247, 26], [248, 26], [249, 26],
        [252, 28], [253, 28], [260, 26], [261, 26], [264, 24], [265, 24], [280, 28],
        [281, 28], [288, 24], [289, 24], [308, 28], [309, 28], [336, 24], [337, 24],
        [360, 36], [361, 36], [375, 36], [376, 36], [378, 36], [379, 36], [384, 32],
        [385, 32], [396, 36], [397, 36], [408, 36], [409, 36], [411, 36], [412, 36],
        [414, 36], [415, 36], [429, 39], [430, 39], [432, 36], [433, 36], [444, 39],
        [445, 39], [447, 39], [448, 39], [449, 32], [462, 42], [463, 42], [468, 36],
        [469, 36], [480, 42], [481, 42], [483, 42], [484, 42], [495, 45], [496, 45],
        [507, 39], [508, 39], [510, 45], [511, 45], [513, 45], [514, 45], [546, 42],
        [547, 42], [576, 48], [577, 48], [585, 45], [586, 45], [588, 42], [589, 42],
        [597, 48], [598, 48], [600, 48], [601, 48], [624, 48], [625, 48], [630, 42],
        [631, 42], [633, 51], [634, 51], [636, 51], [637, 51], [663, 51], [664, 51],
        [672, 48], [673, 48], [708, 48], [709, 48], [750, 51], [751, 51], [900, 60],
        [901, 60], [960, 64], [961, 64], [1020, 68], [1021, 68], [1024, 64], [1025, 64],
        [1216, 64], [1217, 64], [1425, 75], [1426, 75], [1520, 80], [1521, 80]
    ]

    if(palletID == 1):
        for i in singlePallet:
            if(ec == i[0]):
                return i[1]
            else:
                pass
    else:
        for i in doublePallet:
            if(ec == i[0]):
                return i[1]
            else:
                pass

def find_key_by_value(value):
    # Embedded pallets dictionary
    pallets = {
    0: [18, 19, 36, 37, 48, 49],
    1: [84, 85, 87, 88, 112, 113, 126, 127, 140, 141, 168, 169],
    2: [160, 161, 170, 171, 176, 177, 186, 187, 188, 189, 192, 193, 204, 205, 222, 223],
    3: [190, 191, 216, 217, 224, 225, 228, 229, 246, 247, 248, 249, 252, 253],
    4: [200, 201, 240, 241, 260, 261, 280, 281, 360, 361, 375, 376, 378, 379],
    5: [264, 265, 308, 309, 396, 397, 408, 409, 411, 412, 414, 415, 429, 430, 444, 445, 447, 448, 462, 463, 480, 481, 483, 484, 495, 496, 510, 511, 513, 514],
    6: [288, 289, 384, 385, 432, 433, 576, 577, 597, 598, 600, 601, 633, 634, 636, 637],
    7: [468, 469, 507, 508, 546, 547, 585, 586, 624, 625, 663, 664],
    8: [336, 337, 448, 449, 588, 589, 630, 631, 672, 673, 708, 709, 750, 751, 900, 901, 960, 961, 1020, 1021, 1024, 1025],
    9: [1216, 1217, 1425, 1426, 1520, 1521]
    }

    # Search for the value in the dictionary
    for key, values in pallets.items():
        if value in values:
            return key
    return None

pallets = {
    0: [18, 19, 36, 37, 48, 49],
    1: [84, 85, 87, 88, 112, 113, 126, 127, 140, 141, 168, 169],
    2: [160, 161, 170, 171, 176, 177, 186, 187, 188, 189, 192, 193, 204, 205, 222, 223],
    3: [190, 191, 216, 217, 224, 225, 228, 229, 246, 247, 248, 249, 252, 253],
    4: [200, 201, 240, 241, 260, 261, 280, 281, 360, 361, 375, 376, 378, 379],
    5: [264, 265, 308, 309, 396, 397, 408, 409, 411, 412, 414, 415, 429, 430, 444, 445, 447, 448, 462, 463, 480, 481, 483, 484, 495, 496, 510, 511, 513, 514],
    6: [288, 289, 384, 385, 432, 433, 576, 577, 597, 598, 600, 601, 633, 634, 636, 637],
    7: [468, 469, 507, 508, 546, 547, 585, 586, 624, 625, 663, 664],
    8: [336, 337, 448, 449, 588, 589, 630, 631, 672, 673, 708, 709, 750, 751, 900, 901, 960, 961, 1020, 1021, 1024, 1025],
    9: [1216, 1217, 1425, 1426, 1520, 1521]
    }