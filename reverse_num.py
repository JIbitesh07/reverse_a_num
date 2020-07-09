n=int(input("enter a number to be reversed"))
s=0
sign=1
if(n<0):
    sign=-1
    n=n*(-1)
while(n>0):
    r=n%10
    s=r+(s*10)
    n=n//10
if(sign<0):
    s=s*(-1)
print(s)
