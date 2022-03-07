# from tkinter import _MenuIndex
from typing import List, NewType

IndexNum = NewType('IndexNum', int)  # 新しい固有の型用意してわかりやすくする

# whileで書いた場合
# def binary_search(numbers: List[int], value: int) -> IndexNum:
#     left, right = 0, len(numbers)-1
#     while left <= right:
#         print("###")
#         mid = (left + right) // 2  # //でIntの商を出す
#         if numbers[mid] == value:
#             return mid
#         elif numbers[mid] < value:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1  # なのも見つからなかった場合はfaulseとして-1

# リカーシブル(再帰関数)で書いた場合


def binary_search(numbers: List[int], value: int) -> IndexNum:
    def _binary_search(numbers: List[int], value: int, left: IndexNum, right: IndexNum) -> IndexNum:
        if left > right:
            return -1
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid+1, right)
        else:
            return _binary_search(numbers, value, left, mid-1)

    return _binary_search(numbers, value, 0, len(numbers) - 1)


if __name__ == '__main__':
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    print(binary_search(nums, 15))  # 6
