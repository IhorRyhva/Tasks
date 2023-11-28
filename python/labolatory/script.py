key = int(input("Key: "))
text = input("Text: ")
list_text = list(text)
length = len(list_text)
script = ""

while key > 0:
    count = 0
    while  count < len(list_text):
        numberOfLetters = count + 1
        if numberOfLetters % key == 0:
            if(list_text[count] != 0):
                script += list_text[count]
            list_text[count] = 0
        count += 1
    key -= 1

print(script)