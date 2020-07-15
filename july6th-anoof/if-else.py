number1 = int(input("please enter number1 : "))
number2 = int(input("please enter number2 : "))
number12= number1 - number2
number21 =number2 - number1
if number1>number2:
    print(f"{number1} - {number2} is",number12)
else:
    print(f"{number2} - {number1} is",number21)
