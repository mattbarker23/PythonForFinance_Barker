## FILL IN THE EXERCISE BELOW ##
## YOU MAY RUN HW4_LOOPS_TEST.PY TO CHECK YOUR SCORE OUT OF 10 ##
# Q1 (1 point)
# Create a function, exampleOne, which takes one integer input parameter.
# Using a loop, populate an array with all values from 0 up to that integer.
# Example Input Parameter: 5
# Example Output: [0, 1, 2, 3, 4]
array = [1,2,3,4,5]
def exampleOne(one):
    array = list(range(0, one))
    return array


# Q2 (1 point):
# Create a function, exampleTwo, which takes two integer input parameters.
# Using a loop, populate an array with all values from the first integer to the second integer.
# Example Input Parameter: 2, 5
# Example Output: [2, 3, 4]
def exampleTwo(two,three):
    array2 = list(range(two,three))
    return array2


# Q3 (1 point):
# Create a function, exampleThree, which takes two integer input parameters.
# Using a loop, populate an array with all values from the first integer to the second integer, skipping every other number.
# Example Input Parameter: 2, 10
# Example Output: [2, 4, 6, 8]
def exampleThree(four,five):
    array3 = list(range(four,five))
    return array3[::2]

# Q4 (2 points):
# Create a function, exampleFour, which takes an input array
# Using a loop, populate a new array with all values from the input array, starting at the 2nd element, multiplied by the previous element
# Example Input Parameter: [2,3,4,5]
# Example Output: [6,12,20]
def exampleFour(inputArray):
    array4 = inputArray
    n = len(array4)
    array4[0] = array4[0] * array4[1]
    for i in range(1,n-2):
        array4[i] = array4[i] * array4[i+1]
    array4[n-1] = array4[n-2] * array4[n-1]
    array4.pop(n-2)
    return array4

# Q5 (2 points):
# Create a function, exampleFive, which takes an input array
# Using a loop, populate a new array with all values from the input array that are even (hint: % operator)
# Example Input Parameter: [2, 3, 4, 5]
# Example Output: [2, 4]
def exampleFive(input):
    array5 = input
    for num in array5:
        if num % 2 != 0:
            array5.remove(num)
    return array5


# input = [2,3,4,5]
# print(exampleFive(input))

# Q6 (3 points):
# Create a function, exampleSix, which takes two input arrays
# If the two arrays are equal in length, populate a new array with all values from the first input array multiplied by the second 
# If the two arrays are not equal in length, return "!Array Mismatch!"
def exampleSix(inp,inpu):
    n = len(inp)
    n1 = len(inpu)
    if n == n1:
        newArray = []
        for num1, num2 in zip(inp, inpu):
            newArray.append(num1 * num2)
        return newArray
    if n != n1:
        return "!Array Mismatch!"
