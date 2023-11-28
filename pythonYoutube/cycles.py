""" for i in range(-5, 16, 5):
    print("Element:", i)
world = "Hello word"
for i in world:
    if i == 'w':
        print("W exist")
    print(i) """
    
# i = 100
# while i >= 10:
#     print(i)
#     i -= 10

""" work = True

while work:
    user_input = input("Enter word STOP: ")
    if user_input == "STOP":
        work = False
print("While loop is done") """

for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i == 7:
        break
    print("Element i ==", i)
    
for i in "Hello world":
    if i == 'l':
        print(" \"L\" exist")
        break
else:
    print("\"V\" doesn't exist")#Else в такому випадку маж бути на рівні з for-цнклом