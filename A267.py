def binary_search (arr, left, right, x):
    if right >= left:
  
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, left, mid-1, x)

        else:
            return binary_search(arr, mid + 1, right, x)
  
    else:
        return -1

arr = [ 2, 3, 1, 10, 40 ]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)
  
if result != -1:
    print ("Element is present at index % d" % result)
else:
    arr.sort()
    result = binary_search(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
