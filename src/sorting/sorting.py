def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    ai, bi, mi = 0, 0, 0
    while mi < elements:
        if ai >= len(arrA):
            merged_arr[mi] = arrB[bi]
            bi += 1
            mi += 1
            continue
        if bi >= len(arrB):
            merged_arr[mi] = arrA[ai]
            ai += 1
            mi += 1
            continue

        if arrA[ai] == arrB[bi]:
            merged_arr[mi] = arrA[ai]
            ai += 1
            mi += 1
            merged_arr[mi] = arrB[bi]
            bi += 1
            mi += 1
        elif arrA[ai] < arrB[bi]:
            merged_arr[mi] = arrA[ai]
            ai += 1
            mi += 1
        else:
            merged_arr[mi] = arrB[bi]
            bi += 1
            mi += 1

    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    left = start
    right = mid
    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            left += 1
        else:
            value = arr[right]

            # Move the elements before the right index to the right 
            index = right
            while index != left:
                arr[index] = arr[index - 1]
                index -= 1

            arr[left] = value
            left += 1
            right += 1
            mid += 1

        if left >= right:
            right = left + 1

# l and r are inclusive
def merge_sort_in_place(arr, l, r):
    if r - l < 1:
        return
    else:
        mid = (l + r) // 2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid+1, r)
        merge_in_place(arr, l, mid+1, r)

