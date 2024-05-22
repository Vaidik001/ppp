#Python Program to display prime no between range.

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Input the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Display prime numbers within the given range
print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)