N=int(input())
base=3
l=[]
while N>0:
    l.append(str(N%3))
    N=N//3
print(''.join(l)) 
