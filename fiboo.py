# fiboo
s=int(input())
a,b=0,1
print(b,end=' ')
for i in range(1,s):
    h=a+b
    print(h,end=" ")
    a,b=b,h


