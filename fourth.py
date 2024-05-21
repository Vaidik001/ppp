#C Program to Swap Two Number without using third variable

a=10
b=30

print("before swaping A value =",a)
print("before swaping B value =",b)

a = a + b
b = a - b
a = a - b

print("after swaping A value =",a)
print("after swaping B value =",b)