""" word = list("laptop")
word[0] = 'L'
word.append("!")
result = "".join(word)
print(result)# .lower() .upper() .capitalize() (Всі перші букви стають великими) .isupper() .islower() """

text = "football,skate,basketball,drive"
hobbies = text.split(",")

for i in range(0, len(hobbies)):
    hobbies[i] = hobbies[i].capitalize()

result = ", ".join(hobbies)
print(result)
