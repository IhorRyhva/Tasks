text = input("Enter first or second: ")

if text == "first":
    list = input("Enter letters: ")
    len = len(list)
    print(len)
    dict = {}
    for char in list:
        if(char.isalpha()):
            char = char.lower()
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    for letter, time in dict.items():
        print(f"Буква: '{letter}', разів: '{time}'")
            
elif text == "second":
    string = input("Enter word: ")
    split_string = string.split()
    sort_string = [word for word in split_string if len(word) >= 3]
    set_string = set(sort_string)
    my_list = list(set_string)
    my_list.sort()
    lenght = int(len(my_list))
    # dict_string = {'set': my_list}
    # print(dict_string)
    for i in range(lenght):
        print(i + 1,": ", my_list[i], sep="")
else:
    print("Ви ввели щось не те")