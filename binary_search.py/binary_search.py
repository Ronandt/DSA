def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Find the middle index
        mid = (low + high) // 2
        guess = arr[mid]

        # 1. Found it!
        if guess == target:
            return mid
        
        # 2. Guess was too high, move the 'high' pointer left
        if guess > target:
            high = mid - 1
            
        # 3. Guess was too low, move the 'low' pointer right
        else:
            low = mid + 1

    # Target is not in the list
    return -1