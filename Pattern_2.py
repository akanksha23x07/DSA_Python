# Print Pattern 1
# AAA
# BBB
# CCC

print("------Pattern 1-----")
n = int(input("Enter value of N: "))
char = "A"
for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(ord(char)+i-1), end="")
    print()
        
# Print Pattern 2
# ABC
# ABC
# ABC

print("------Pattern 2-----")
n = int(input("Enter value of N: "))
for i in range(1, n+1):
    char = 'A'
    for j in range(1, n+1):
        print(chr(ord(char)+j-1), end="")
    print()

# Print Pattern 3
# ABC
# DEF
# GHI

print("------Pattern 3-----")
n = int(input("Enter value of N: "))
char = 'A'
k =1
for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(ord(char)+k-1), end="")
        k+=1
    print()

# Print Pattern 4
# ABC
# BCD
# CDE

print("------Pattern 4-----")
n = int(input("Enter value of N: "))
char = 'A'
for i in range(1, n+1):
    k =i
    for j in range(1, n+1):
        print(chr(ord(char)+k-1), end="")
        k+=1
    print()

# Print Pattern 4-method-2
# ABC
# BCD
# CDE

print("------Pattern 4-method-2-----")
n = int(input("Enter value of N: "))
char = 'A'
for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(ord(char)+i+j-2), end="")
    print()
    
# Print Pattern 5
# A
# BB
# CCC

print("------Pattern 5-----")
n = int(input("Enter value of N: "))
char = 'A'
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(ord(char)+i-1), end="")
    print()
        

# Print Pattern 6
# A
# BC
# DEF

print("------Pattern 6-----")
n = int(input("Enter value of N: "))
char = 'A'
k = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(ord(char)+k-1), end="")
        k+=1
    print()

# Print Pattern 7
# A
# BC
# CDE

print("------Pattern 7-----")
n = int(input("Enter value of N: "))
char = 'A'
for i in range(1, n+1):
    k=i
    for j in range(1, i+1):
        print(chr(ord(char)+k-1), end="")
        k+=1
    print()

# Print Pattern 7-method-2
# A
# BC
# CDE

print("------Pattern 7-method-2-----")
n = int(input("Enter value of N: "))
char = 'A'
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(ord(char)+i+j-2), end="")
    print()

# Print Pattern 8
# A
# BC
# CDE

print("------Pattern 8-----")
n = int(input("Enter value of N: "))
char = 'A'
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(ord(char)+n-i+j-1), end="")
    print()

# Print Pattern 9
#    *
#   **
#  ***

print("------Pattern 9-----")
n = int(input("Enter value of N: "))
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(' ',end='')
    for k in range(1, i+1):
        print("*",end='')
    print()
        
        
# Print Pattern 10
# xxx
# xx
# x

print("------Pattern 10-----")
n = int(input("Enter value of N: "))
for i in range(1, n+1):
    for j in range(n-i+1):
        print('x',end='')
    print()

# Print Pattern 11
# xxxx
#  xxx
#   xx
#    x

print("------Pattern 11-----")
n = int(input("Enter value of N: "))
for i in range(1, n+1):
    for j in range(i-1):
        print(' ',end='')
    for k in range(n-i+1):
        print('x',end='')
    print()


# Print Pattern 12
# xxxx
#  xxx
#   xx
#    x

print("------Pattern 12-----")
n = int(input("Enter value of N: "))
for i in range(1, n+1):
    for j in range(i-1):
        print(' ',end='')
    for k in range(n-i+1):
        print(i,end='')
    print()

# Print Pattern 13
# xxxx
#  xxx
#   xx
#    x

print("------Pattern 13-----")
n = int(input("Enter value of N: "))
for i in range(1, n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        print(i,end='')
    print()

# Print Pattern 14
# 1234
#  234
#   34
#    4

print("------Pattern 14-----")
n = int(input("Enter value of N: "))
for i in range(1, n+1):
    l=i
    for j in range(i-1):
        print(' ',end='')
    for k in range(n-i+1):
        print(l,end='')
        l+=1
    print()

# Print Pattern 15
# 1234
#  234
#   34
#    4

print("------Pattern 15-----")
n = int(input("Enter value of N: "))
l=1
for i in range(1, n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        print(l,end='')
        l+=1
    print()

# Print Pattern 16
# ---1---
# --121--
# -12321-
# 1234321

print("------Pattern 16-----")
n = int(input("Enter value of N: "))
for i in range(1, n+1):
    g=i
    for j in range(n-i):
        print(" ",end="")
    l=1
    for k in range(i-1):
        print(l,end='')
        l+=1
    for m in range(i):
        print(g,end='')
        g-=1
    print()

# Print Pattern 16-Method-2
# ---1---
# --121--
# -12321-
# 1234321

print("------Pattern 16-Method-2-----")
n = int(input("Enter value of N: "))
for i in range(1, n+1):
    g=i-1
    for j in range(n-i):
        print(" ",end="")
    l=1
    for k in range(i):
        print(l,end='')
        l+=1
    for m in range(i-1):
        print(g,end='')
        g-=1
    print()

# Print Pattern 17
# ---1---
# --121--
# -12321-
# 1234321

print("------Pattern 17-----")
n = int(input("Enter value of N: "))
for i in range(1, n+1):
    g = 1
    for j in range(n-i+1):
        print(g,end="")
        g+=1
    for k in range(i-1):
        print("*",end='')
    for l in range(i-1):
        print("*",end='')
    o=n-i+1
    for m in range(n-i+1):
        print(o,end='')
        o-=1

    print()
        
        





