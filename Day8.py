#dictionry
birthday = {
    "Adarsha B M": "03-03-2003",
    "Amith": "07-12-2004",
    "virat":"05-10-1988"
}

print(birthday.get("Adarsha B M", "Not Found"))

birthday["Sudeep"] = "02-09-1903" #addind
birthday["Sudeep"] = "02-09-1973" #update

#birthday.pop("Adarsha B M") #remove

print(birthday)

print(birthday.keys())
print(birthday.values())
print(birthday.items())