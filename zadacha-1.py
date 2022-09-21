a=int(input())
n=int(input())
if a<0 and n>=-a:
    print (a+n+1)
elif a>0 and n<=-a:
    print (a+n-1)
else:
    print (a+n)