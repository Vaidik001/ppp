# Write a c program to create a student's mark sheet and calculate total & percentage
#Create a student's mark sheet and find grades according to percentage
#print("hello world")

#a=10;
#b=20;

#value enter    
print("enter subject marks out of 100")
a=float(input("enter java marks:"))
b=float(input("enter dbms marks:"))
c=float(input("enter python marks:"))

#display value
print("java=",a)
print("dbms=",b)
print("python=",c)

#totle value
total=a+b+c
print("total marks=",total)

#total par
par=int(total*100/300)
print("par=",par,"%")

def g(par):
    if par >= 90:
        return 'A'
    elif par >= 80:
        return 'B'
    elif par >= 70:
        return 'C'
    elif par >= 60:
        return 'D'
    elif par >= 50:
        return 'E'
    else:
        return 'fail'
grade = g(par)
print("grade=",grade)

