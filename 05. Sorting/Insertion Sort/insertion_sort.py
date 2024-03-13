# Insertion Sort Algorithm

"""
Complexity Analysis of Insertion Sort:

## Time Complexity of Insertion Sort
1. The worst-case time complexity of the Insertion sort is O(N^2)
2. The average case time complexity of the Insertion sort is O(N^2)
3. The time complexity of the best case is O(N).

## Space Complexity of Insertion Sort
1. The auxiliary space complexity of Insertion Sort is O(1)

## Characteristics of Insertion Sort
1. This algorithm is one of the simplest algorithms with a simple implementation
2. Basically, Insertion sort is efficient for small data values
3. Insertion sort is adaptive in nature, i.e. it is appropriate for data sets that are already partially sorted.
"""

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print("Sorted array is:", sorted_arr)
