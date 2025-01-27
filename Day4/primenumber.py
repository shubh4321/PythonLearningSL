n=int(input("Enter Any Number "))
i=1
isPrime = True

for i in range(2,n):
    if(n%2==0):
        isPrime = False
        break

if(isPrime):
    print("Prime Number")
else:
    print("Not Prime Number")
