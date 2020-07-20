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
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
