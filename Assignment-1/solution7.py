romanRepresentation = {'one':'I','two':'II','three':'III','four':'IV','five':'V','six':'VI','seven':'VII','eight':'VIII','nine':'IX','ten':'X'}
print(romanRepresentation)
print('for (press 0 to exit )\nlen()-1 \t\t clear()-2 \ncopy()-3 \t\t fromkeys()-4')
print('get()-5 \t\t items()-6')
print('keys()-7 \t\t pop()-8')
print('popitem()-9 \t\t setdefault()-10')
print('update()-11 \t\t values()-12')
while True:
    choice = int(input('Enter your choice: '))
    if choice==0:
        break
    elif choice==1:
        print(len(romanRepresentation))
    elif choice==2:
        romanRepresentation.clear()
        print("the dictionary is:",romanRepresentation)
    elif choice==3:
        x = romanRepresentation.copy()
        print(x,'is the copied dictionary')
    elif choice==4:
        key = input('Enter a key')
        value = input('Enter a value:')
        x = romanRepresentation.fromkeys(key,value)
        print(x)
    elif choice==5:
        x = input('Enter a key from dictionary:')
        print("the corossponding value is:",romanRepresentation.get(x))
    elif choice==6:
        print(romanRepresentation.items())
    elif choice==7:
        print(romanRepresentation.keys())
    elif choice==8:
        x = input("Enter a key:")
        romanRepresentation.pop(x)
        print(romanRepresentation)
    elif choice==9:
        romanRepresentation.popitem()
        print(romanRepresentation)
    elif choice==10:
        x = input('enter a key:')
        y = input('enter a value:')
        romanRepresentation.setdefault(x,y)
        print(romanRepresentation)
    elif choice==11:
        x = input('enter a key:')
        y = input(' enter a value:')
        romanRepresentation.update({x:y})
        print(romanRepresentation)
    elif choice==12:
        print(romanRepresentation.values())
    else:
        print('invalid input')
