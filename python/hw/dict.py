developer = {"name": "Bill", 
             "surname": "Heyts", 
             "experienceExist": True, 
             "age": 68, "wealth":                
             "many money", 
             "myAttitude":""}

attitude = input("Your attitude: ")

if attitude == "I hate everybody":
    del developer["name"]
else:
    developer["myAttitude"] = attitude
print(developer["myAttitude"])

inputKey = input("Enter: key or value or items: ")
if inputKey == "key":
    keys = developer.keys()
    print("Keys: ", keys)
elif inputKey == "value":
    values = developer.values()
    print("Value: ", values)
elif inputKey == "items":  
    allDev = developer.items()
    print("allDev: ", allDev)

reaction = input("Stop or Continue: ")
if reaction == "Stop":
    developer.clear()
    print("Stop")
elif reaction == "Continue":
    lenght = len(developer)
    print(lenght)
else:
    print("You enter incorrect reaction")