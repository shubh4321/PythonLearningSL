def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact = fact*i
    return fact

print("4!=", factorial(4))
print("5!=", factorial(5))
print("6!=", factorial(6))
print("9!=", factorial(9))
