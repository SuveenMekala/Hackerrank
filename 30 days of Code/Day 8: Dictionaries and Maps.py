import sys

n=int(input().strip())
phoneBook={}
for i in range(n):
    S=(input().split())
    #print(S)
    phoneBook[S[0]]=S[1]
#print(phoneBook)
while True:
    k= str(input())
    if k not in phoneBook:
        print('Not found')
    else:
        print((k+'='+phoneBook[k]))
