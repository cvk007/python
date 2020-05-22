oddNumbers = list()
for number in range(1,101):
    if number%2!=0: oddNumbers.append(number)
sumOfOddNumbers=0
for number in oddNumbers:
    sumOfOddNumbers+=number
print(oddNumbers)
print('the sum is:',sumOfOddNumbers)
