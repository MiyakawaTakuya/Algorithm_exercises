from typing import List
# 217. Contains Duplicate 220407
# Runtime: 721 ms, faster than 21.96 % of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26.1 MB, less than 32.21 % of Python3 online submissions for Contains Duplicate.
# リストの要素を昇順または降順 https: // www.javadrive.jp/python/list/index11.html  # section1
# 重複を消したlist https://www.sejuku.net/blog/21923


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newlist = sorted(nums)
        for i in range(len(newlist) - 1):
            if newlist[i] == newlist[i+1]:
                return True
        return False

    def containsDuplicateA(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False


solution = Solution()
nums = [1, 2, 3, 1]
print(solution.containsDuplicate(nums))
nums = [1, 2, 3, 4]
print(solution.containsDuplicate(nums))
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(solution.containsDuplicate(nums))
print(solution.containsDuplicateA(nums))
