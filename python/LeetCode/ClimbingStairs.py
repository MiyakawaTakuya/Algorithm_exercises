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

    # Approach 1: Brute Force
    def climbStairsA(self, n: int) -> int:
        def _climb_Stairs(i: int, n: int) -> int:
            if i > n:
                return 0
            if i == n:
                return 1
            return _climb_Stairs(i+1, n) + _climb_Stairs(i+2, n)
        return _climb_Stairs(0, n)
# Algorithm
# In this brute force approach we take all possible step combinations i.e. 1 and 2, at every step.
# At every step we are calling the function climbStairsclimbStairs for step 11 and 22,
# and return the sum of returned values of both functions.
# climbStairs(i, n) = (i + 1, n) + climbStairs(i + 2, n)climbStairs(i, n) = (i+1, n)+climbStairs(i+2, n)
# where ii defines the current step and nn defines the destination step.


solution = Solution()
a = 6
print(solution.climbStairsA(a))


# normal fibonacci
#     def climbStairs(self, n: int) -> int:
#         if n < 3:
#             return 1
#         else:
#             return self.climbStairs(n - 2) + self.climbStairs(n - 1)
