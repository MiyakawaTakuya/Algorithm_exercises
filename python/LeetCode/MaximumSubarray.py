from typing import List
# 53. Maximum Subarray 220408
# find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum. A subarray is a contiguous part of an array.
# 連続した部分配列（少なくとも1つの数値を含む）の総和の最大値を見つけ、その総和を返しなさい。


# WIP
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


solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.
print(solution.maxSubArray(nums))
nums = [1]
print(solution.maxSubArray(nums))
nums = [5, 4, -1, 7, 8]
print(solution.maxSubArray(nums))
nums = [-2, -1]  # -1
print(solution.maxSubArray(nums))
[0, -3, 1, 1]  # 2
print(solution.maxSubArray(nums))
