gg,nn=map(int,input().split())
dd=list(map(int,input().split()))
vv=[]
for i in dd:
 if(i<=i+1):
  vv.append(i)
print(vv[nn-1])
