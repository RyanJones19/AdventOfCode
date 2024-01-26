import sys
import time

input = open(sys.argv[1]).read().strip().split('\n\n')

def compare_packets(packet1: list, packet2: list) -> bool:
    #print()
    print("New compare")
    if len(packet1) == 0:
        return True
    while packet1 and packet2:
        #time.sleep(1)
        print(f"packet1: {packet1}")
        print(f"packet2: {packet2}")
        comparator1 = packet1.pop(0)
        comparator2 = packet2.pop(0)
        print(f"comparator1: {comparator1}")
        print(f"comparator2: {comparator2}")
        #print(f"len(packet1): {len(packet1)}")
        #print(f"len(packet2): {len(packet2)}")

        cmp1Type = type(comparator1)
        cmp2Type = type(comparator2)

        if cmp1Type == list and len(comparator1) == 0 and cmp2Type == list and len(comparator2) != 0:
            return True
        elif cmp1Type == list and len(comparator1) == 0 and cmp2Type == list and len(comparator2) == 0:
            if len(packet1) > len(packet2):
                return False
            else:
                continue
        elif cmp2Type == list and len(comparator2) == 0:
            return False

        if cmp1Type == int and cmp2Type == int:
            if comparator1 < comparator2:
                return True
            elif comparator1 == comparator2:
                if len(packet1) == 0 and len(packet2) == 0:
                    continue
                elif len(packet1) == 0:
                    return True
                elif len(packet2) == 0:
                    #print("Return false 0")
                    return False
                else:
                    continue
            else:
                #print("Return false 1")
                return False

        elif cmp1Type == list and cmp2Type == list:
            returnVal = compare_packets(comparator1, comparator2)
            #print(f"returnVal: {returnVal}")
            #print(f"len(packet1): {len(packet1)}")
            #print(f"len(packet2): {len(packet2)}")
            return returnVal if returnVal is not None else False if len(packet2) == 0 else True
            #return compare_packets(comparator1, comparator2)
            #if compare_packets(comparator1, comparator2):
            #    return True
            #else:
            #    print("Return false 2")
            #    continue
                #return False

        elif cmp1Type == int and cmp2Type == list:
            comparator1 = [comparator1]
            return compare_packets(comparator1, comparator2)

        elif cmp1Type == list and cmp2Type == int:
            comparator2 = [comparator2]
            return compare_packets(comparator1, comparator2)


correct_orders = 0
for i, item in enumerate(input):
    if i == 26:
        print(item)
    packet1, packet2 = item.split('\n')
    if compare_packets(eval(packet1), eval(packet2)):
        print(f"CORRECT order: {i + 1}")
        #print()
        correct_orders += i + 1
    else:
        print(f"INCORRECT order: {i + 1}")
        #print()

print(f"Part 1: {correct_orders}")
