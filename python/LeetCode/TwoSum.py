from typing import List, Final


class Solution:
    def twoSum(self, nums, target) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

# 以下は全てコード練習用
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    # TypeError: 'type' object is not subscriptable type' オブジェクトは添え字を付けられない
    def twoSum3(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    def twoSumStr(self, nums: list, target: int):
        new_list = []
        for i in range(len(nums)):
            new_list.append(nums[i])
        return new_list


# 定数の書き方
TABLE_NAME: Final[str] = 'sample'
# TABLE_NAME='あいう'  →エラー

nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))
print(solution.twoSum2(nums, target))
nums_str = ['2', '7', '11', '15']
print(solution.twoSumStr(nums_str, target))
