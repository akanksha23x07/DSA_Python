# This Program contains Recursive Binary Search Implementation:


def Print(arr, start, end):
    for i in range(start, end+1):
        print(arr[i], end=' ')
    print(' ')
        

def binSearch(arr, start, end, target):
    Print(arr, start, end)
    # base case
    if start>end:
        return False, -1
    mid = start+((end-start)//2)
    if arr[mid] == target:
        return True, mid
    if arr[mid] > target: # BS left pe 
        return binSearch(arr, start, mid-1, target)
    else:
        return binSearch(arr, mid+1, end, target) #BS right pe

# Main
arr = [6, 7, 18, 20]
found, index= binSearch(arr, 0, len(arr)-1, 18)
print("Element Found: ", found, index)
        
    
