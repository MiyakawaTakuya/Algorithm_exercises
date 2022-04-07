from typing import List
from collections import deque
import numpy as np
# 238. Product of Array Except Self  220407
# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# 18 / 20 test cases passed. Status: Time Limit Exceeded


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if j != i:
                    num *= nums[j]
            products.append(num)
        return products


# スタックとキュー 方法 https://qiita.com/saba/items/107c4237206e31acdbef
# listでの利用は遅いので注意！！しかも参照ができないので不便
# collections.dequeが良さそう append() 末尾に追加  popleft() 先頭を取り出す [0]で先頭を参照
# Success
# Runtime: 635 ms, faster than 5.02 % of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 39.6 MB, less than 5.33 % of Python3 online submissions for Product of Array Except Self.

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        d = deque()
        products = []
        productsAll = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                productsAll *= nums[i]
            else:
                d.append(i)  # 0の数値が入っているnumsのインデックスをキューで保管
        if len(d) == 0:  # 0が一つもなかった場合は気にせずに計算していく
            for i in range(len(nums)):
                products.append(int(productsAll/nums[i]))
            return products
        elif len(d) == 1:
            for i in range(len(nums)):
                if i != d[0]:
                    products.append(0)
                else:
                    products.append(productsAll)
            return products
        elif len(d) >= 2:
            array = np.empty(len(nums), dtype=int)
            array.fill(0)
            return array


# Approach 1: Left and Right product lists
# range関数の逆 range(10, 0, -1)   -> 10 9 8 7 6 5 4 3 2 1

    def productExceptSelfA(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # The left and right arrays as described in the algorithm
        left, right, answer = [0]*length, [0]*length, [0]*length
        # print(left)  initialize array filled 0 all
        left[0] = 1
        for i in range(1, length):
            left[i] = left[i-1]*nums[i-1]
        # print(left)
        right[length - 1] = 1
        for i in reversed(range(length-1)):  # except last(=nums[0]) index
            right[i] = right[i+1]*nums[i+1]
        # print(right)
        for i in range(length):
            answer[i] = left[i] * right[i]
        return answer


# Approach 2: O(1) space approach
# Runtime: 280 ms, faster than 65.48 % of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21 MB, less than 96.56 % of Python3 online submissions for Product of Array Except Self.

    def productExceptSelfB(self, nums: List[int]) -> List[int]:
        # The length of the input array
        length = len(nums)
        # The answer array to be returned
        answer = [0]*length
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):
            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer


solution = Solution()
nums = [1, 2, 3, 4]  # Output: [24,12,8,6]
print(solution.productExceptSelfB(nums))
nums = [-1, 1, 0, -3, 3]
print(solution.productExceptSelfB(nums))
