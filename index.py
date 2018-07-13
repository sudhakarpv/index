# index
n=int(input())
l=[]
for i in range (n):
    l.append(input())
for k in l:
    print(k,l.index(k),sep=" ")
