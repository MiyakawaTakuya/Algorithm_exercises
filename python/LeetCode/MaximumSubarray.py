from typing import List
# 53. Maximum Subarray 220408
# find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum. A subarray is a contiguous part of an array.
# 連続した部分配列（少なくとも1つの数値を含む）の総和の最大値を見つけ、その総和を返しなさい。


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        # Sum = sum(nums)
        L, R = [0]*length, [0]*length
        maxFromL, maxFromR, sumL, sumR, indexL, indexR = -10000, -10000, 0, 0, 0, 0
        for i in range(length):
            sumL += nums[i]
            L[i] = sumL
            if sumL > maxFromL:
                maxFromL = sumL
        for i in reversed(range(length)):
            sumR += nums[i]
            R[i] = sumR
            if sumR > maxFromR:
                maxFromR = sumR
        indexL = L.index(maxFromL)
        indexR = R.index(maxFromR)
        newSum = 0
        maxCenter = -10000
        for i in range(indexR, indexL + 1):
            newSum += nums[i]
            if newSum > maxCenter:
                maxCenter = newSum
        return max(max(nums), maxCenter)


# Approach 1: Optimized Brute Force   →Time Limit Exceeded
# Algorithm
# Initialize a variable maxSubarray = -infinity to keep track of the best subarray.
# We need to use negative infinity, not 0, because it is possible that there are only negative numbers in the array.
# Use a for loop that considers each index of the array as a starting point.
# For each starting point, create a variable currentSubarray = 0. Then, loop through the array from the starting index,
# adding each element to currentSubarray. Every time we add an element it represents a possible subarray
# - so continuously update maxSubarray to contain the maximum out of the currentSubarray and itself.
# Return maxSubarray.


    def maxSubArrayA(self, nums: List[int]) -> int:
        max_subarray = -float('inf')   # -math.inf → error
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        return max_subarray

# Approach 2: Dynamic Programming, Kadane's Algorithm
    def maxSubArrayA2(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray


solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.
print(solution.maxSubArrayA2(nums))
nums = [1]
print(solution.maxSubArrayA2(nums))
nums = [5, 4, -1, 7, 8]
print(solution.maxSubArrayA2(nums))
nums = [-2, -1]  # -1
print(solution.maxSubArrayA2(nums))
nums = [0, -3, 1, 1]  # 2
print(solution.maxSubArrayA2(nums))
