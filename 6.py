b,jn=map(int,input().split())
df=input().split()
h=[]
for i in df:
 if(int(i)%2!=0):
  h.append(i)
print(h[jn-1])
