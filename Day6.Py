#list

items= ["bru","sugar","milk","bru"]
print(items)
print(type(items))
print(items[0])

items.pop() #remove last element
print(items)

items.pop(0) #remove frist element
print(items)

items.append("parle-g",) #add elment
print(items)

items.remove("sugar") #remove particular element
print(items)

items.insert(0,"spoon") #add particular element
print(items)

items[0] = "cofee" #replace particular element
print(items)