""" nums = [5,  7, 4.63, 10]

for el in nums:
    res = el * 2
    print(res) """
    
user_count_hobby = int(input("Enter number hobby: "))
i = 0
hobby = []
while i < user_count_hobby:
    text = "Enter hobby" + str(i + 1) + ": "
    hobby.append(input(text))
    i += 1
print(hobby)