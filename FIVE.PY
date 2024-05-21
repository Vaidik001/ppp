#C Program to Check Whether a Number is Even or Odd

num= int(input("enter number="))


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


result = check_even_odd(num)

print("numbrer is",result)
