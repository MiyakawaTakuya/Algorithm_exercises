# 70. Climbing Stairs  20220409
# 20220410
# Runtime: 24 ms, faster than 98.59% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.9 MB, less than 14.27 % of Python3 online submissions for Climbing Stairs.

class Solution:
    def climbStairs(self, n: int) -> int:
        def fibona(a: int, b: int, n: int) -> int:
            if n < 3:
                return a
            return fibona(a+b, a, n-1)

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return fibona(2, 1, n)


solution = Solution()
a = 5
print(solution.climbStairs(a))

# normal fibonacci
#     def climbStairs(self, n: int) -> int:
#         if n < 3:
#             return 1
#         else:
#             return self.climbStairs(n - 2) + self.climbStairs(n - 1)
