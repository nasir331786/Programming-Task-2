"""Problem 6: XOR Operation in an Array
LeetCode Problem #1486
Difficulty: Easy

Given an integer n and an integer start.
Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums.

Example 1:
    Input: n = 5, start = 0
    Output: 8
    Explanation: nums = [0, 2, 4, 6, 8]
                 0 ^ 2 ^ 4 ^ 6 ^ 8 = 8

Example 2:
    Input: n = 4, start = 3
    Output: 8
    Explanation: nums = [3, 5, 7, 9]
                 3 ^ 5 ^ 7 ^ 9 = 8

Example 3:
    Input: n = 1, start = 7
    Output: 7
    Explanation: nums = [7]
                 7 = 7
"""


class Solution:
    """Solution to XOR Operation in an Array problem."""
    
    def xorOperation(self, n: int, start: int) -> int:
        """
        Create array where nums[i] = start + 2*i, return XOR of all elements.
        
        Time Complexity: O(n)
        Space Complexity: O(1) - not counting the output array
        
        Args:
            n: Number of elements
            start: Starting value
            
        Returns:
            Bitwise XOR of all generated array elements
        """
        result = 0
        for i in range(n):
            result ^= (start + 2 * i)
        return result
    
    def xorOperationWithArray(self, n: int, start: int) -> int:
        """
        Alternative approach - explicitly create array first.
        
        Time Complexity: O(n)
        Space Complexity: O(n) - for storing the array
        
        Args:
            n: Number of elements
            start: Starting value
            
        Returns:
            Bitwise XOR of all generated array elements
        """
        nums = [start + 2 * i for i in range(n)]
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ((5, 0), 8),
        ((4, 3), 8),
        ((1, 7), 7),
        ((10, 5), 2),
    ]
    
    for (n, start), expected in test_cases:
        result = solution.xorOperation(n, start)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: xorOperation(n={n}, start={start}) = {result}")
