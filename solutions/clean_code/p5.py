class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        for digit in str(n):
            digit_val = int(digit)
            product *= digit_val
            total += digit_val
        return product - total
sol = Solution()
print(sol.subtractProductAndSum(234))
print(sol.subtractProductAndSum(4421))
