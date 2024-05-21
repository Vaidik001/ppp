#C program to calculate Simple interest. ✓ Simple interest = (amount* rate* time)/100

amount = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

print("amount=",amount)
print("rate=",rate)
print("time=",time)

interest = (amount* rate* time)/100

print("Total interest=",interest)
