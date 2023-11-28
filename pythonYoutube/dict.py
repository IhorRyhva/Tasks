person = {"name": "Alex", "age": 15, 5: 12, True: "False", (4, 7): 45}#ключем може бути все що завгодно крім масиву
""" #person[5] = "Five"
print(person[5])

person1 = dict(name = "Alex", age = 15)
# print(person1["name"])

for key, values in person.items():
    print(key, values, sep="-")
    
for el in person.values():
    print(el)
    
for el in person.keys():
    print(el) """

#print(person.get("name"))
""" person.clear() """
#person.popitem()
#person.pop(5)
person['bio'] ='Text'
print(person)