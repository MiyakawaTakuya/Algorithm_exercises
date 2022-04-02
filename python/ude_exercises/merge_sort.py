from typing import List


def merge_sort(numbers: List[int]) -> List[int]:
    # 要素が１つになるまで細分化していき、１つになったときにその箱を返す
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2  # //でInt(整数)にしてくれる
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)  # この処理で箱が１つになるまで細分化して、そこから順次マージしていく
    merge_sort(right)

    i = j = k = 0  # iが左に分割された半分のインデックス、jが右半分、kは結合した後の箱全体
    while i < len(left) and j < len(right):  # 一番右の１つの箱以外全て充填するwhile
        if left[i] < right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):  # 残りの一番右の箱を充填するwhile
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):  # 残りの一番右の箱を充填するwhile
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(nums)
    print(merge_sort(nums))
