def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Division by zero not possible")

number1 = float(input('Enter number 1:'))
number2 = float(input('Enter number 2:'))
div(number1,number2)

def open_file(file):
    try :
        fhand = open(file)
        for line in fhand:
            print(line,end="")
    except FileNotFoundError:
        print("File not found")

file = input("Enter file name:")
open_file(file)