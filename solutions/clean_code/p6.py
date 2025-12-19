class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= (start + 2 * i)
        return result
sol = Solution()
print(sol.xorOperation(5, 0))
print(sol.xorOperation(4, 3))
print(sol.xorOperation(1, 7))
