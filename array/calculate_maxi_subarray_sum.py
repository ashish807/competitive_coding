'''
Given an array of numbers, :find the maximum sum of any contiguous subarray of
the array. For example, given the array [34, -50, 42, 14, -5, 86], the maximum
sum would be 137, since we would take elements 42, 14, -5, and 86. Given the array
[ -5, -1, -8, -9], the maximum sum would be 0, since we would choose not to
take any elements.
'''
def maximum_sum(nums: list):
    sum_till_now, maximum_sum = 0, -float("inf")
    for num in nums:
        sum_till_now = max(num, num+sum_till_now)
        maximum_sum = max(sum_till_now, maximum_sum)
    print(maximum_sum)
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    maximum_sum(nums)
