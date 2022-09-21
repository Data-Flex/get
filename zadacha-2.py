a=int(input())
b=int(input())
c=int(input())
if min(4*a,2*b,4*c)==4*a:
    print (4*a)
elif min(4*a,2*b,4*c)==2*b:
    print (2*b+1)
else:
    print (4*c+2)