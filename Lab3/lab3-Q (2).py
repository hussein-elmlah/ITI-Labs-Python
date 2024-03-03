class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n == 1 or n == 2:
            return n
        prev = 1
        res = 2
        for i in range(3,n+1):
            temp = res
            res += prev
            prev = temp
        return res