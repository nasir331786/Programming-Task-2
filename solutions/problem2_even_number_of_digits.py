"""Problem 2: Find Numbers with Even Number of Digits
LeetCode Problem #1295
Difficulty: Easy

Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:
    Input: nums = [12,345,2,6,7896]
    Output: 2
    Explanation: 12 contains 2 digits, 7896 contains 4 digits

Example 2:
    Input: nums = [555,901,482,1771]
    Output: 1
    Explanation: Only 1771 contains 4 digits
"""

from typing import List


class Solution:
    """Solution to Find Numbers with Even Number of Digits problem."""
    
    def findNumbers(self, nums: List[int]) -> int:
        """
        Count how many numbers in the array have an even number of digits.
        
        Time Complexity: O(n*m) where n is array length and m is average digit count
        Space Complexity: O(1)
        
        Args:
            nums: Array of integers
            
        Returns:
            Count of numbers with even digit count
        """
        count = 0
        for num in nums:
            # Convert to string to count digits, use abs() for negative numbers
            if len(str(abs(num))) % 2 == 0:
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([12, 345, 2, 6, 7896], 2),
        ([555, 901, 482, 1771], 1),
        ([1, 22, 333, 4444], 2),
    ]
    
    for nums, expected in test_cases:
        result = solution.findNumbers(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: findNumbers({nums}) = {result}")
