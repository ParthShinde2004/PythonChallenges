def linear_search(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return "not found"

List = ['a','b','c','d','r','i','z','l']
x = 'f'
print("Element Found in List at index:" + str(linear_search(List,x)))
