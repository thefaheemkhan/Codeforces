# Selection Sort Algorithm - Select Minimum

"""
## Complexity Analysis of Selection Sort
Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:

1. One loop to select an element of Array one by one = O(N)
2. Another loop to compare that element with every other Array element = O(N)
3. Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)
4. Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. The selection sort never makes more than O(N) swaps and can be useful when memory writing is costly. 

## Advantages of Selection Sort Algorithm
1. Simple and easy to understand.
2. Works well with small datasets.

## Disadvantages of the Selection Sort Algorithm
1. Selection sort has a time complexity of O(n^2) in the worst and average case.
2. Does not work well on large datasets.
3. Does not preserve the relative order of items with equal keys which means it is not stable.

"""

def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
