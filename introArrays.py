text = "Utah man am I. Kayay!"

textArray = [ "Utah", "man", "am", "I", ]

len(textArray)

textCapitalized = []
for char in textArray:
    textCapitalized.append( char.capitalize() )

print(textCapitalized)
# print(textArray[0],textArray[3])

#Utes we are
textArray[0] = "Utes"
textArray[1] = "we"
textArray[2] = "are"
variable = textArray.index("I")

# print(textArray.pop(3))
print(textArray.remove("I"))
emptyArray = []
emptyArray.append("element1")
emptyArray.append("element2")
# print(returnVariable)
firstNames = ["John", "Jack", "Mary"]
lastNames = ["Fisher", "Cook", "Smith"]

for index in range( 0, len(firstNames) ):
    lastNames.reverse()
    print(firstNames[index],lastNames[index])

print( list( range( len(firstNames) ) ) )

print(emptyArray)

def e(array2):
    newArray = []
    for element in аrrаy2[-5:]:
         if еlеment % 5 == 0: break
         newАrray.аppend(еlеmеnt)

array2 = [1,2,3,4,5,6,7,8,9]
print(e(array2))