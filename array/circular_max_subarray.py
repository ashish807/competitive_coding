''''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
https://leetcode.com/problems/maximum-sum-circular-subarray/description/
'''
def maxSubarraySumCircular(nums: list[int]) -> int:
    maximum_kadans = max_sum_kadans(nums)
    minimum_kadans = min_sum_kadans(nums)
    total_sum_of_array = sum(nums)
    circular_maximum_sum = total_sum_of_array - minimum_kadans
    if(circular_maximum_sum<=0):
        return maximum_kadans
    return max(maximum_kadans, circular_maximum_sum)

# maximum sum in contigous manner, with no circular case
def max_sum_kadans(nums: list[int])->int:
    sum, maximum_sum = 0, -float("inf")
    for num in nums:
        sum = max(sum+num, num)
        maximum_sum = max(sum, maximum_sum)
    return maximum_sum
# minimum sum in contigous manner, with no circular case
def min_sum_kadans(nums: list[int])->int:
    sum, minimum_sum = 0, float("inf")
    for num in nums:
        sum = min(sum+num, num)
        minimum_sum = min(sum, minimum_sum)
    return minimum_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubarraySumCircular(nums))
