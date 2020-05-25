word = input('Enter a string: ')
arr = dict()
for i in range(len(word)):
    arr[word[i]] = arr.get(word[i],0) + 1
a =list()
for k,v in arr.items():
    a.append((v,k))
a = sorted(a,reverse=True)
for i in range(len(a)):
    x = a[i]
    t = int(x[0])
    y = x[1]
    print(y*t,end="")
