from typing import List
# Pythonのリストの要素のインデックス（何番目か）を取得 https://note.nkmk.me/python-list-index/
# range関数 https://www.javadrive.jp/python/function/index6.html
# max() min()のインデックス https://hibiki-press.tech/python/max_min_index/586


class Solution:
    #スライス方式では参照できない問題が多発してしまった. 通過できてないコード
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        min_ = min(prices[:len(prices)-1])
        a = max(prices[prices.index(min_):]) - min_
        max_ = max(prices[1:])
        b = max_ - min(prices[:prices.index(max_)])
        if max(a, b) < 0:
            return 0
        else:
            return max(a, b)

    # Approach 1  必要最小限で数値を比較して最大値を求める
    def maxProfitA(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):  # 長さから1引いた分の要素数を見る. →最後のインデックスを除いた範囲でbuyの候補をあたる
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

    # Apprioach 2 Time complexity: O(n). Only a single pass is needed.
    def maxProfitB(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit


solution = Solution()
prices = [7, 1, 5, 3, 6, 2]
print(solution.maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(solution.maxProfit(prices))

# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Input: prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
