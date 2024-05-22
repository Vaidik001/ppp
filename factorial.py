#Python program to Find factorial of no.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Input the number from the user
num= int(input("Enter a number to find its factorial: "))

print("Factorial of", num, "is", factorial(num))