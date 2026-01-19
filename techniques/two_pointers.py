CONDITION = True
def fn(arr):
    ans = 0
    left = 0
    right = len(arr) - 1
    while left < right:
        # TODO: logic with left and right
        if CONDITION:
            left += 1
        else:
            right -= 1
    return ans
"""
Assumptions

3. When is this technique valid?

Two pointers work when:

✅ The array is sorted

or

✅ The problem has monotonic behavior

Meaning:

If something is too small, moving right increases it

If something is too large, moving left decreases it

This monotonicity lets you safely eliminate choices.
"""