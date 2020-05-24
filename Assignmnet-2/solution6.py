word1 = input("Enter first string :")
word2 = input("Enter second string:")
dictOfWord1 = dict()
dictOfWord2 = dict()
for i in range(len(word1)):
    dictOfWord1[word1[i]] = dictOfWord1.get(word1[i],0)+1

for i in range(len(word2)):
    dictOfWord2[word2[i]] = dictOfWord2.get(word2[i],0)+1

a=sorted(dictOfWord1.items())
b=sorted(dictOfWord2.items())

if a==b:
    print('Yes')
else:
    print('NO')