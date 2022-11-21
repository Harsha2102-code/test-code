valid=['1','2','3','5','8','9','0']
n=int(input())
c,i=0,0
while c!=n:
    x=[k for k in str(i) if k not in valid]
#     print(x)
    if len(x)==0:
        c+=1
    i+=1
print(i)
