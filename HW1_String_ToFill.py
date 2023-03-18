## FILL IN THE EXERCISE BELOW ##
## YOU MAY RUN HW1_STRING_TEST.PY TO CHECK YOUR SCORE OUT OF 10 ##




# Q1 (1 point)
# Prompt: Please create a function, exampleOne, which returns: "Lorem Ipsum!"
def exampleOne():
    result1 = "Lorem Ipsum!"
    return result1

# Q2 (1 point)
# Prompt: Please create a function, exampleTwo, which takes one input paramter and returns it encolosed in parathensis
# Example Input Parameter: "Ipsum"
# Example Output: "(Ipsum)"
def exampleTwo(one):
    result2 = "({})".format(one)
    return result2

# Q3 (1 point)
# Prompt: Please create a function, exmpleThree, which takes two input paramters. Please return "This %parameter1% and that %parameter2%"
# Example Input Parameters: "Duis", "Aute"
# Example Out: "This Duis and that Aute"
def exampleThree(two,three):
    result3 = "This {} and that {}".format(two,three)
    return result3

# Q4 (1 point)
# Prompt: Please create a function, exampleFour, that will have two input parametesr. First one is a string you need to adjust, and second is the leading and
# trailing text that needs to be removed
# Example Input: "++++++consectetur adipiscing elit+++++++", "+"
# Example Output: "consectetur adipiscing elit"
def exampleFour(four,five):
    result4 = four.strip(five)
    return result4

# Q5 (3 points)
# Prompt: Please create a function, exampleFive, that will help calcualte our age in dog years. This function will take one input parameter, an integer.
# Recall, to get your age in dog years you simply have to divide your age by 7. Please return "In dog years, I am %parameter1 / 7%. But, in human years I am %parameter1%"
# Example Input: 24.5
# Example Output: "In dog years, I am 3.5. But, in humans years I am 24.5"

def exampleFive(param):
    param = float(param)
    result5 = "In dog years, I am {}. But, in humans years I am {}".format(str(param/7),str(param))
    return result5

# Q6 (3 points)
# Prompt: Please creata a function, exampleSix, with one input parameter. Please return the input parameter with all vowels removed.
# i.e a, e, i, o, u, and sometimes y
# Example Input: "Lorem ipsum dolor sit amet"
# Example Output: "Lrm psm dlr st mt"
def exampleSix(seven):
    result6 = seven.replace("a", "")
    result6 = result6.replace("e", "")
    result6 = result6.replace("i", "")
    result6 = result6.replace("o", "")
    result6 = result6.replace("u", "")
    return result6
