# Bubble Sort Algorithm -- Push the max to the last by adjacent swaps

"""
## Complexity Analysis of Bubble Sort:
1. Time Complexity: O(N2)
2.  Auxiliary Space: O(1)

## Advantages of Bubble Sort:
1. Bubble sort is easy to understand and implement.
2. It does not require any additional memory space.
3. It is a stable sorting algorithm, meaning that elements with the same key value 
maintain their relative order in the sorted output.

## Disadvantages of Bubble Sort:
1. Bubble sort has a time complexity of O(N2) which makes it very slow for large data sets.
2. Bubble sort is a comparison-based sorting algorithm, which means that it requires a 
comparison operator to determine the relative order of elements in the input data set. 
It can limit the efficiency of the algorithm in certain cases.
"""

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr = [64, 25, 12, 22, 11]
sorted = bubble_sort(arr)
print(sorted)