a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if a > b and a > c and a > d:
    print("The largest number is ", a)

elif b > a and b > c and b > d:
    print("The largest number is ", b)

elif c > a and c > b and c > d:
    print("The largest number is ", c)

else:
    print("The largest number is ", d)