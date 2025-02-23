#find factorial using a function(def)
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

a=int(input("enter a number:"))
y=fact(a)
print("factorial of given number is=",y)
