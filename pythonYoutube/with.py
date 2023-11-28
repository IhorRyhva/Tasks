try:
    with open('data/myfile.txt', 'r', encoding='utf-8') as file:
        print(file.read())#Автоматично закриває файл
except FileNotFoundError:
    print('Ви ввели щось не те')