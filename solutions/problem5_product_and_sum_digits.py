"""Problem 5: Subtract the Product and Sum of Digits of an Integer
LeetCode Problem #1281
Difficulty: Easy

Given an integer number n, return the difference between the product of its digits
and the sum of its digits.

Example 1:
    Input: n = 234
    Output: 15
    Explanation: Product of digits = 2 * 3 * 4 = 24
                 Sum of digits = 2 + 3 + 4 = 9
                 Result = 24 - 9 = 15

Example 2:
    Input: n = 4421
    Output: 21
    Explanation: Product of digits = 4 * 4 * 2 * 1 = 32
                 Sum of digits = 4 + 4 + 2 + 1 = 11
                 Result = 32 - 11 = 21
"""


class Solution:
    """Solution to Subtract Product and Sum of Digits problem."""
    
    def subtractProductAndSum(self, n: int) -> int:
        """
        Calculate product of digits and sum of digits, return their difference.
        
        Time Complexity: O(log n) where log n is the number of digits
        Space Complexity: O(1)
        
        Args:
            n: A positive integer
            
        Returns:
            Difference between product and sum of digits
        """
        product = 1
        total = 0
        
        for digit in str(n):
            digit_val = int(digit)
            product *= digit_val
            total += digit_val
        
        return product - total
    
    def subtractProductAndSumMath(self, n: int) -> int:
        """
        Alternative approach using mathematical operations.
        
        Time Complexity: O(log n) where log n is the number of digits
        Space Complexity: O(1)
        
        Args:
            n: A positive integer
            
        Returns:
            Difference between product and sum of digits
        """
        product = 1
        total = 0
        
        while n > 0:
            digit = n % 10
            product *= digit
            total += digit
            n //= 10
        
        return product - total


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        (234, 15),
        (4421, 21),
        (1, 0),
    ]
    
    for n, expected in test_cases:
        result = solution.subtractProductAndSum(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: subtractProductAndSum({n}) = {result}")
