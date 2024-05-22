#Python program to find GCD and LCM of two no. Greatest Common Divisor (GCD) and Least Common Multiple (LCM)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Input the two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and print GCD and LCM
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))
print("LCM of", num1, "and", num2, "is:", lcm(num1, num2))



import math

# Input the two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and print GCD and LCM
print("GCD of", num1, "and", num2, "is:", math.gcd(num1, num2))
print("LCM of", num1, "and", num2, "is:", (num1 * num2) // math.gcd(num1, num2))