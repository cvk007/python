arr=list()
print('\n1 ) Peep \t 2 ) Pop \t 3 ) Push 4) show whole list\n 0 to quit')
while True:
    option = input('Enter your option:')
    if option == '0':
        break
    elif option == '1':
        if len(arr) <=0:
            print("No element in list")
        else:
            print('the element is : ',arr[len(arr)-1])
    elif option == '2':
        if len(arr)<=0:
            print('cannot pop from empty list')
        else:    
            arr.remove(arr[len(arr)-1])
            print("removed")
    elif option =='3':
        x = input('Enter the element you want to insert:')
        arr.append(x)
    elif option=='4':
        print(arr)
    else:
        print(" Invalid option")
