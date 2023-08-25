fruit ={
    "name":"orange",
    "weight":"10kg"
}
print ( fruit)
print ("the name of the fruit is " ,fruit["name"])
print ("the weight of the fruit is " ,fruit["weight"])
fruit ["name"] = "apple"
print ("the name of the fruit is " ,fruit["name"])
print ( len(fruit))
fruit ["quality"] = "good"
print ( fruit)
del  fruit ["weight"]
print ( fruit)
fruit.pop("quality")
fruit.update({"price" : "3d"})
fruit.update({"name" : "strawberries"})
#fruit.clear()
print(fruit)
print ("all the keys" ,fruit.keys())
print("all the values", fruit.values())
print(fruit.get("name"))
