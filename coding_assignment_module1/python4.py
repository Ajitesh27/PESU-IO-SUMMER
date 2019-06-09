print("Welcome to program 4")
x=int(input("Enter the number "))
sum=0
while x>0:
    s=x%10
    x=int(x/10)
    sum=sum+s
print("sum is ",sum)
