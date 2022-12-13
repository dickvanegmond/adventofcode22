with open('day13/input.txt') as f:
    lines = f.read().splitlines() 

pairs = []
for i in range(0,len(lines), 3):
    pairs.append((eval(lines[i]), eval(lines[i+1])))

from itertools import zip_longest

def compareValues(leftSequence, rightSequence):
    for left, right in zip_longest(leftSequence, rightSequence):
        # print(left, right)
        # If left < right and both int return True
        if (isinstance(left, int) and isinstance(right, int)) and left < right:
            # print("LEFT SMALLER")
            return True

        # If left > right and both int return False
        if (isinstance(left, int) and isinstance(right, int)) and left > right:
            # print("RIGHT SMALLER")
            return False
            

        # If left is None, return True
        if left == None:
            # print("LEFT NONE")
            return True

        # If right is None, return False
        if right == None:
            # print("RIGHT NONE")
            return False

        # If one is list, other int. make Int list
        if (isinstance(left, int) and isinstance(right, list)):
            # print("RIGHT LIST, LEFT INT")
            left = [left]
        
        if (isinstance(right, int) and isinstance(left, list)):
            # print("LEFT LIST, RIGHT INT")
            right = [right]
        
        if (isinstance(right, list) and isinstance(left, list)):
            # print("GOING DEEPR")
            returnValue = compareValues(left, right)
            
            if returnValue == True:
                return True
            elif returnValue == False:
                return False

        # print("NEXT NUMBER")

sumIndices = 0
for count, pair in enumerate(pairs, start=1):
    if compareValues(pair[0],pair[1]):
        sumIndices += count

# Answer Part 1    
print(sumIndices)

signals = [eval(line) for line in lines if line != ""]

signals.append([[2]])
signals.append([[6]])
print(signals)

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if not compareValues(arr[j], arr[j+1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

bubbleSort(signals)
print("SORTED")

# Answer Part 2
print((signals.index([[2]])+1) * (signals.index([[6]])+1))