# print pattern 1
# ****
# ****
# ****
# ****

print("-------Pattern 1-----")
n = int(input("Enter value of n: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end = '')
    print()

# Print Pattern 2
# 1234
# 1234
# 1234
# 1234

print("-------Pattern 2-----")
n = int(input("Print n: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end = '')
    print()

# Print Pattern 3
# 111
# 222
# 333

print("-------Pattern 3-----")
n = int(input("Print n: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i, end = '')
    print()

# Print Pattern 4
# 321
# 321
# 321
print("-------Pattern 4------")
n =int(input("Enter n: "))
for i in range(1, n+1):
    num = n
    for j in range(1, n+1):
        print(num, end = "")
        num -= 1
    print()

# Print Pattern 4-2
# 321
# 321
# 321
print("-------Pattern 4-Method-2------")
n =int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(n, 0, -1):
        print(j, end = "")
    print()

# Print Pattern 5
# 123
# 456
# 789

print("-------Pattern 5------")
k=1
n =int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(k," ", end = "")
        k+=1
    print()

# Print Pattern 6
# *
# **
# ***
# ****

print("-------Pattern 6------")
n =int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end = "")
    print()

# Print Pattern 7
# 1
# 12
# 123
# 1234

print("-------Pattern 7------")
k=1
n =int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = "")
    print()

# Print Pattern 8
# 1
# 12
# 123
# 1234

print("-------Pattern 8------")
n =int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end = "")
    print()

# Print Pattern 9
# 1
# 12
# 123
# 1234

print("-------Pattern 9------")
k=1
n =int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(k, end = "")
        k+=1
    print()

# Print Pattern 10
# 1
# 23
# 345
# 4567

print("-------Pattern 10------")
n =int(input("Enter n: "))
for i in range(1, n+1):
    k=i
    for j in range(1, i+1):
        print(k, end = "")
        k+=1
    print()

# Print Pattern 10-method-2
# 1
# 23
# 345
# 4567

print("-------Pattern 10-method-2------")
n =int(input("Enter n: "))
for i in range(0, n):
    for j in range(0, i+1):
        print(i+j+1, end = "")
    print()

# Print Pattern 11
# 1
# 23
# 345
# 4567

print("-------Pattern 11------")
n =int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end = "")
    print()

# Print Pattern 11-method-2
# 1
# 23
# 345
# 4567

print("-------Pattern 11-method-2------")
n =int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i-j+1, end = "")
    print()





