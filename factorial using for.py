#find factorial using for loop
n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of given number is=",fact)
