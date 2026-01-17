def quick_sort(arr: list) -> list:
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n // 2] #assume pivot to be in the centrre
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort(arr, low, high):
    if low < high:
        # 1. Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # 2. Recursively sort the left side
        quick_sort(arr, low, pivot_index - 1)

        # 3. Recursively sort the right side
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # We choose the last element as the pivot
    pivot = arr[high]
    [3,5,7,1,2]
    # 'i' tracks the "boundary" of items smaller than the pivot
    i = low - 1
    
    for j in range(low, high): #stops before high the FINAL POINT
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1
            # Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
    
    # Finally, swap the pivot element into its correct sorted place
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the position where the pivot ended up
    return i + 1 #correct because we never acccouned for the +1 just now (the final one )

# To use it:
# data = [10, 7, 8, 9, 1, 5]
# quick_sort(data, 0, len(data) - 1)

"""
The "Generalized" Version
If we put the pivot inside the loop, the code looks like this:
code
Python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    # We go all the way to 'high' (including the pivot)
    for j in range(low, high + 1): 
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Look! No final swap needed outside the loop anymore.
    return i
Does it work? Yes.
Let's trace your example [3, 5, 7, 1, 2] with this generalized logic:
j=0 to 2 (3, 5, 7): Nothing happens. i is still -1.
j=3 (Value 1): 1 ≤ 2 is True. i becomes 0. Swap index 0 and 3.
Array: [1, 5, 7, 3, 2]
j=4 (Value 2 - The Pivot): 2 ≤ 2 is True.
i becomes 1.
Swap arr[i] (index 1, value 5) with arr[j] (index 4, value 2).
Array: [1, 2, 7, 3, 5]
Return i (1). The pivot is at index 1. It works perfectly!"""

#It moves the larger ones up while moving the pivot to see whether the end is bigger than the rest of the numbers 
#If it's smaller it moves the pivot one more up for the number
"""
3. A Visual Example of the "Shift"
Imagine the pivot is 5.
Current state: [2, 3, | 8, 9, 7, | 1, 5]
Zone A (Smalls): 2, 3 (End at i)
Zone B (Bigs): 8, 9, 7 (This is the "buffer" between i and j)
j is now looking at 1.
The Logic: 1 is smaller than 5.
Move the "wall" i forward. Now i points at the 8.
Swap 8 and 1.
Array becomes: [2, 3, 1, | 9, 7, 8, | 5]
"""
"""
So the theory is that the main pointer will STOP if J encounters a larger number but will MOVE and swap(which is the smaller zone)
Whenever J moves adn I doesn't move It knows that those numbers are already bigger than the p[ivot ] So if it moves one more it is guaranteed that it swaps with a smaller number 
"""