"""
Your module description
"""
myFruitList=["apple","banana","cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
myFruitList[2]="orange"
print(myFruitList)
myFinalANswerTuple=("apple","banana","pineapple")
print(myFinalANswerTuple)
print(type(myFinalANswerTuple))
#myFinalANswerTuple[2]="mango"
myFruitDictionary = { "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"}
print(myFruitDictionary)
print(type(myFruitDictionary))
print(myFruitDictionary["Akua"])
myFruitDictionary["Akua"]="mango"
print(myFruitDictionary)


myMixedTypeList = [45, 29057856564665, 1.02, True, "My dog is on the bed.", "45"]
print(myMixedTypeList)


for item in myMixedTypeList:
    print("{} is data type {}".format(item,type(item)))
    