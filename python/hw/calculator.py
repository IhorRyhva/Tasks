num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
action = input("Enter action: ")
res = 0

cycles = True
while cycles:
    if action == '+':
        res = num1 + num2
        print(res)
        cycles = False
    elif action == '-':
        res = num1 - num2
        print(res)
        cycles = False
    elif action == '/':
        if  num2 != 0:
            res = num1 / num2
            print(res)
            cycles = False
        else:
            print("Ти не можеш ділити на нуль")
            cycles = False
    elif action == '*':
        res = num1 * num2
        print(res)
        cycles = False
    elif action == '%':
        res = num1 % num2
        print(res)
        cycles = False
    else:
        print("You forgot entered action")
        cycles = False