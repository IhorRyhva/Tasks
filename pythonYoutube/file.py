# data = input("Enter your hobby: ")

file = open('data/myfile.txt', 'r')#w - записати щось в файл #a додає і НЕ видаляє старе #r- читає файл
# file.write(data + '\n')
""" print(file.read(10))# считується 10 символів, якщо цього не написати то будуть считані всі данні """
for line in file:
    print(line, end='')
file.close()