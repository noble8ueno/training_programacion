def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]

    print("Original list:", numbers)
    sorted_numbers = bubble_sort(numbers)
    print("Sorted list:", sorted_numbers)
