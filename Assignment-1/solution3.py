lowerLimitOfRange = int(input('Enter lower limit of range :'))
upperLimitOfRange = int(input('Enter upper limit of range :'))

for number in range(lowerLimitOfRange,upperLimitOfRange+1):
    flag=0
    for divisor in range(2,number):
        if number%divisor==0:
            flag=1
            break
    if flag==0:
        print(number)
