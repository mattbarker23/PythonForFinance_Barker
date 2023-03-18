#SPQR - Senatus Populus Que Romanus
array = []
array.append("Senatus")
array.append("Populus")
array.append("Que")
array.append("Romanus")
print(array[1])
print(array)

dict = {}
dict["S"] = "Senatus"
dict["P"] = "Populus"
dict["Q"] = "Que"
dict["R"] = "Romanus"
# print(dict["P"])
# print(dict)

arrayTwo = [ "one", "two", "three", "four" ]
dictionary = {"one":"ein", "two":"zwei","three":"drei"}

# print( dictionary.keys() )
# print( dictionary.values() )
# print( dictionary.items() )

# value = dictionary.pop("one")
# dictionary.clear()
# print(dictionary, "Popped Element: ",value)

valueOne = dictionary.get("three","Not Found")
valueOneOne = dictionary["three"]

dictionary["four"] = dictionary.get("four","Not Found") + " or maybe Chetyre"
# print(valueOne,valueTwo)

for key,value in dictionary.items():
    print(key,value)

for key in dictionary:
    print(key,dictionary[key])
