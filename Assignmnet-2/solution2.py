def fabonnaci(n):
    if n <= 1 :
        return n
    else:
        return (fabonnaci(n-1) + fabonnaci(n-2))

n = int(input('Enter n: '))
for i in range(n):
    print(fabonnaci(i), end=" ")