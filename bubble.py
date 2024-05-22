#Write a program to sort the list elements using bubble sort technique.


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Set a flag to detect any swap
        swapped = False
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break

# Example usage
original_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(original_list)
print("Sorted list is:", original_list)