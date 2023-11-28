key = int(input("Key: "))
text = input("Text: ")
list_text = list(text)
length = len(list_text)
script = ""

lengthNewList = int(length / 2)
lengthNewListTwo = int(length / 3)
            
if(key % 2 == 0):
    count = key / 2
    count = int(count)
    for i in range(count):
        first = []
        second = []
        for i in range(length):
            if(i < lengthNewList):
                second += list_text[i]
            else:
                first += list_text[i]

        a = 0
        b = 0
        for i in range(length):
            numberOfNumber = i + 1
            if(numberOfNumber % 2 != 0):
                list_text[i] = first[a]
                a += 1
            else:
                list_text[i] = second[b]
                b += 1
    for i in range(length):
        script += list_text[i]

else:

    first = []
    second = []
    third = []
    for i in range(length):
        numberOfNumber = i + 1
        if(numberOfNumber <= lengthNewListTwo):
            third += list_text[i]
        elif(numberOfNumber > lengthNewListTwo and numberOfNumber < (lengthNewListTwo * 3 - 1)):
            second += list_text[i]
        else:
            first += list_text[i]

    a = 0
    b = 0
    c = 0
    for i in range(length):
        numberOfNumber = i + 1
        if(numberOfNumber <= lengthNewListTwo):
            list_text[i] = first[a]
            a += 1
        elif(numberOfNumber > lengthNewListTwo and numberOfNumber < (lengthNewListTwo * 3 - 1)):
            list_text[i] = second[b]
            b += 1
        else:
            list_text[i] = third[c]
            c += 1
            
for i in range(lengthNewListTwo):
    for element in list_text:
        script += (element[i])
          
                
print(script)


             
         