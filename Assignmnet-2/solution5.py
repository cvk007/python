n = int(input('Enter total number of numbers:'))
numbers = input().split()
arr = list()
for i in range(n):
    arr.append(int(numbers[i]))
print(arr)

arr.sort()

print(arr)

def binarysearch(arr,starting,ending,asked):
    if ending >= starting:
        mid = starting + (ending -starting)//2
        if arr[mid] == asked:
            return mid
        elif arr[mid] > asked :
            return binarysearch(arr,starting,mid-1,asked)
        else:
            return binarysearch(arr,mid+1,ending,asked)
    else:
        return -1

asked = int(input('Enter a number:'))
x = binarysearch(arr,0,len(arr)-1,asked)
if x==-1:
    print("Number not found")
else:
    print("Number found at index :",x)