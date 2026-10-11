# Task 1

a = int(input())
b = int(input())

if a > b:
    print("Maximum =", a)
    print("Minimum =", b)
else:
    print("Maximum =", b)
    print("Minimum =", a)

# Task 2

n = int(input())

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Task 3

# a = int(input())
# b = int(input())
# c = int(input())

# minimum, middle, maximum = sorted([a, b, c])

# print("Maximum =", maximum)
# print("Minimum =", minimum)
# print("Middle =", middle)


a = int(input())
b = int(input())
c = int(input())

# Maximum
if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

# Minimum
if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

# Middle
if (a >= b and a <= c) or (a <= b and a >= c):
    middle = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    middle = b
else:
    middle = c

print("Maximum =", maximum)
print("Minimum =", minimum)
print("Middle =", middle)


# Task 4

h = int(input("Hours = "))
m = int(input("Minutes = "))

if h >= 0 and h <= 23 and m >= 0 and m <= 59:
    print("Valid Time")
else:
    print("Invalid Time")

# Task 5

x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print("1 quadrant")
elif x < 0 and y > 0:
    print("2 quadrant")
elif x < 0 and y < 0:
    print("3 quadrant")
elif x > 0 and y < 0:
    print("4 quadrant")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("Y axis")
else:
    print("X axis")

# Task 6

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == b and b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)    

# Task 7

n = int(input())

d1 = n // 1000          # thousands digit
d2 = (n // 100) % 10    # hundreds digit
d3 = (n // 10) % 10     # tens digit
d4 = n % 10             # ones digit

total = d1**4 + d2**4 + d3**4 + d4**4

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# Task 8

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

if a <= d and c <= b:
    print("Overlapping")
else:
    print("Not Overlapping")

# Task 9

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

# Task 10

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

if x1 == x2 and y1 == y2:
    print("NO")
elif x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")





