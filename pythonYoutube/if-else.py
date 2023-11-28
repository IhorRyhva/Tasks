number = int(input("Enter number: "))
isHasCar = True
if number > 55 or not isHasCar: #and = &&, or = ||
    print("Yes")
    if number == 100:
        print("Number equals 100!!!")
elif number == 40:# elif може бути безліч
    print("number = 40")
else:
    print("Yes, of course")
        
isHappy = True  #Якщо хочу написати що він False, то можна написати if not isHappy:
if isHappy:
    print("Yes, he is happy!")    
print("More text")