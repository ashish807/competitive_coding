''''
Given an array of integers that are out of order, determine the bounds of the smallest
window that must be sorted in order for the entire array to be sorted. For example,
given [ 3 , 7 , 5 , 6 , 9] , you should return ( 1 , 3 ).
'''
def locate_smallest_window_to_sort(nums: list)->int:
    left, right = None, None
    max_seen, min_seen = -float("inf"), float("inf")
    for i in range(len(nums)):
        max_seen = max(max_seen, nums[i])
        if nums[i] < max_seen:
            left = i
    for i in range(len(nums)-1, -1, -1):
        min_seen = min(min_seen, nums[i])
        if nums[i] > min_seen:
            right = i
    
    ans = abs(left-right) + 1 if left is not None and right is not None else 0
    return ans

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print(locate_smallest_window_to_sort(nums))
