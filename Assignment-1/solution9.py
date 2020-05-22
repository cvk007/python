string = input("Enter a string:")
temp=""
i=len(string)-1
while i>=0:
    temp+=string[i]
    i=i-1
if string==temp:
    print('True')
else:
    print('False')
