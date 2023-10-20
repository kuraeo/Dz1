num = int(input("Знайти факторіал для числа: "))
factorial = 1    
if num > 0:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)
elif num == 0:    
   print("1")
else:    
   print("Факторіалу від'ємного числа не існує")
