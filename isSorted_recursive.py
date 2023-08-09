# Checking if an array is sorted using recursion
def isSorted(arr, size):
    # Base Case
    if size == 0 or size == 1:
        return True
    if arr[0]>arr[1]:
        return False
    # Recursive call
    else:
        ans = isSorted(arr[1:], size-1)
        return ans
arr = [1,2,3,4,5,8, 6,7]
size = len(arr)
sortd = isSorted(arr, size)
print('Array is sorted: ', sortd)
    
