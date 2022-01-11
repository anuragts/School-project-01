# Write a program in python for Binary Search
#Recursive function

def binary_search(arr, left, right, x):

    if right >= left:

        mid = (right + left) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)

   
        else:
            return binary_search(arr, mid + 1, right, x)

    else:
        return -1




arr = list(map(int, input("Enter a sorted array - ").rstrip().split()))
x = int(input("Enter the element to be searched - "))
left = 0
right = len(arr) - 1
if __name__ == '__main__':
    result = binary_search(arr, left, right, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
