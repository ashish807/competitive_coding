'''
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Given an array of integers, return a new array where each element in the new array
is the number of smaller elements to the right of that element in the original input
array.
For example, given the array [ 3, 4, 9, 6, 1], return [ 1, 1, 2, 1, 0], since:
• There is 1 smaller element to the right of 3
• There is 1 smaller element to the right of 4
• There are 2 smaller elements to the right of 9
• There is 1 smaller element to the right of 6
• There are no smaller elements to the right of 1
'''
import bisect
def countSmaller(nums: list[int]):
    sorted_list = [nums[-1]]
    final_list = [0 for _ in range(len(nums))]
    for num in range(len(nums)-2, -1, -1):
        index = bisect.bisect_left(sorted_list, nums[num])
        final_list[num] = index
        bisect.insort(sorted_list, nums[num])
    print(final_list)
countSmaller([1,9,7,8,5])