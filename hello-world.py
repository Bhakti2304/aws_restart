print('Hello,World')
print("Hello, Bhakti")


print("Python has three numeric types: int, float, and complex")
myValue0=23
myValue1=23.4
myValue2=23j
myValue3=True
myValue="Amazon Web Services"
print(myValue)
print(str(myValue) +" is of the data type " + str(type(myValue)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print(name)
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
myFruitList[2] = "orange"
print(myFruitList)

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
#myFinalAnswerTuple[2] = "mango"
#print(myFinalAnswerTuple)

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    