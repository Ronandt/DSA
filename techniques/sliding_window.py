def max_sum_fixed(arr, k):
    n = len(arr)
    if n < k:
        return None

    # 1. Compute the sum of the very first window
    window_sum = sum(arr[:k])
    max_val = window_sum

    # 2. Slide the window from left to right
    for i in range(n - k):
        # Subtract the element "falling out" of the window (left)
        # Add the element "entering" the window (right)
        window_sum = window_sum - arr[i] + arr[i + k]
        
        max_val = max(max_val, window_sum)

    return max_val

# Example: [1, 2, 3, 4, 5, 6], k=3
# Window 1: [1, 2, 3] sum=6
# Window 2: [2, 3, 4] sum=9 (Subtract 1, Add 4)
# Window 3: [3, 4, 5] sum=12 (Subtract 2, Add 5)


def min_subarray_dynamic(arr, target):
    min_length = float('inf')
    current_sum = 0
    start = 0

    for end in range(len(arr)):
        # 1. EXPAND: Add the next element to the window
        current_sum += arr[end]

        # 2. CONTRACT: While the condition is met, shrink from the left
        # to find the "smallest" version of this valid window
        while current_sum >= target:
            # Calculate length of current window
            window_size = end - start + 1
            min_length = min(min_length, window_size)
            
            # Remove the leftmost element and move the start pointer
            current_sum -= arr[start]
            start += 1

    return min_length if min_length != float('inf') else 0

# Example: [2, 3, 1, 2, 4, 3], target=7
# Window expands until [2, 3, 1, 2] (sum 8 >= 7)
# Window then shrinks from left: [3, 1, 2] (sum 6 < 7) -> Stop shrinking
# Window expands again...