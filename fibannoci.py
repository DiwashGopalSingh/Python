a = 0
b = 1
i = 0
n = int(input("Enter the total number of values: "))
while i < n:
    print(a, end = " ")
    c = a + b
    a = b
    b = c
    i += 1