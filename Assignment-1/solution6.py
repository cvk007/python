numbers=list(range(1,21))
even=list()
odd=list()
for num in numbers:
    if num%2 !=0 :
        odd.append(num)
    else:
        even.append(num)
print('even numbers in list:',even)
print('odd numbers in list: ',odd)
