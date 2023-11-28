# num = None
# while num is None:
#     try:
#         num = int(input("Enter: "))
#         num += 5
#         print(num)
#     except ValueError:
#         print("Ви ввели щось не те")
try:
    a = 10
    b = int(input("Enter num: "))
    print(a / b)
except ValueError: #Exception перевіряє на всі можливі помилки
    print("Ypu enter incorect value!!!!!")
except ZeroDivisionError:
    print("На нуль ділити не можна")
else:
    print("Ви молодець")
finally:
    print("Finally")