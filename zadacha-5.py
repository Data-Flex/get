a=int(input())
b=int(input())
n=0
for i in range (a,b+1):
    if (i%10+i//10%10+i//100%10+i//1000%10+i//10000%5)%2!=0:
        n+=1
print (n)