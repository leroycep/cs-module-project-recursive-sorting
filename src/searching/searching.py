def binary_search(arr, target, start, end, ascending=True):
    if start > end:
        return -1
    mid = (start + end) // 2
    if target == arr[mid]:
        return mid
    elif (ascending and target > arr[mid]) or not ascending and target < arr[mid]:
        return binary_search(arr, target, mid + 1, end, ascending)
    elif (ascending and target < arr[mid]) or (not ascending and target > arr[mid]):
        return binary_search(arr, target, start, mid - 1, ascending)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    ascending_order = arr[0] < arr[len(arr)-1]
    return binary_search(arr, target, 0, len(arr), ascending=ascending_order)
