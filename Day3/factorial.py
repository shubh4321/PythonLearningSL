n = int(input("Enter number to find Factorial: "))

fact = 1
for i in range (1,n+1):
    fact = fact*i

print("Factorial of ",n ,"is",fact)
