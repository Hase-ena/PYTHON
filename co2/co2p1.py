def factorial(x):
    if x == 1:
        return 1
    else:
        return(x*factorial(x-1))
n = int(input("Enter a number:"))
print("Factorial of",n,":",factorial(n))