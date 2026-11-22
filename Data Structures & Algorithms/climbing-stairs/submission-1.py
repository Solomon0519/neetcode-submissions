class Solution:

    computed = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        
        if self.computed.get(n, 0) != 0:
            return self.computed[n]
        else:
            result = self.climbStairs(n - 2) + self.climbStairs(n - 1) 
            self.computed[n] = result
            return result
