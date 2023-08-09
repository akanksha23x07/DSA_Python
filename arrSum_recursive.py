# Program to find sum of elemnts of an array using recursion:

def sum(arr, size):
    # Base Case
    if size == 0:
        return 0
    if size == 1:
        return arr[0]
    
    # Recursive Call
    remainingPart = sum(arr[1:], size-1)
    return remainingPart + arr[0]

# Main
arr = [1,2,3,4,5,6]
size = len(arr)
ans2 = sum(arr, size)
print('Sum of arr is: ', ans2)
