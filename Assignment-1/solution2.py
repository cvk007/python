number1 = int(input("Enter number1 :"))
number2 = int(input("Enter number2 :"))
number3 = int(input("Enter number3 :"))
if number1==number2==number3:
    print('all are the same')
elif number1 >= number2 and number1 >= number3:
    print(number1,'is the greatest')
elif number2 >= number1 and number2 >= number3 :
    print(number2,'is the greatest')
elif number3 >= number2 and number3 >= number1:
    print(number3,'is the greatest')
