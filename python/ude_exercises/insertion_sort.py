from typing import List
#見る値を都度適切な位置まで持っていくソート

def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1,len_numbers):
        tmp = numbers[i]
        j = i - 1 #jは見比べるときのカーソルの位置
        while j >= 0 and numbers[j] > tmp:
            numbers[j+1] = numbers[j]
            j -= 1  #tmpの値を適切な位置まで左にスライドさせるためjを1ずつ減らしていく
        numbers[j+1]=tmp
        
    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(insertion_sort(nums))
