#sort values of three variable in ascending order

a = 5
b = 2
c = 8


if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print("Sorted values in ascending order:", a, b, c)