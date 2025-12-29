#tupple

genders = ("male","female","other")
print(genders)
print(type(genders))

#set
s ={1, 2 ,3}
print(s)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 | s2) # union
print(s1 & s2) #intersection
print(s1 - s2)#difference

r = {1, 2, 3}
r.add(4)
#r.remove(10)
r.discard(10)
r.pop()
print(r)