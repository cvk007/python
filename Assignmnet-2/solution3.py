def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
while True:
    number1 = float(input('Enter number 1 :'))
    number2 = float(input('Enter number 2 :'))
    print('Operations are:\n 1 ) Addition\n2 ) Subtraction\n3 ) Multiplication \n4 ) Division \n5 ) Modulus \n To exit press 0 in operation')
    operator = input("Enter opeartaion :")

    if operator =='0':
        break
    elif operator == '1':
        print(add(number1,number2))
    elif operator == '2':
        print(sub(number1,number2))
    elif operator == '3':
        print(mul(number1,number2))
    elif operator == '4':
        print(div(number1,number2))
    elif operator == '5':
        print(mod(number1,number2))
    else:
        print("Invalid Choice !")

