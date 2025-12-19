from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(abs(num))) % 2 == 0:
                count += 1
        return count

sol = Solution()
print(sol.findNumbers([12, 345, 2, 6, 7896]))
print(sol.findNumbers([555, 901, 482, 1771]))
