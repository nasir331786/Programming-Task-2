"""Problem 3: Number of Good Pairs
LeetCode Problem #1512
Difficulty: Easy

Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: Pairs (0,3), (0,4), (3,4), (2,5) are good

Example 2:
    Input: nums = [1,1,1,1]
    Output: 6
    Explanation: All pairs are good
"""

from typing import List


class Solution:
    """Solution to Number of Good Pairs problem."""
    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Count pairs (i, j) where nums[i] == nums[j] and i < j.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        
        Args:
            nums: Array of integers
            
        Returns:
            Count of good pairs
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
    
    def numIdenticalPairsOptimized(self, nums: List[int]) -> int:
        """
        Optimized approach using frequency count.
        If value x appears n times, number of pairs = n * (n - 1) / 2
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Args:
            nums: Array of integers
            
        Returns:
            Count of good pairs
        """
        from collections import Counter
        freq = Counter(nums)
        count = 0
        for num_count in freq.values():
            count += num_count * (num_count - 1) // 2
        return count


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
    ]
    
    for nums, expected in test_cases:
        result = solution.numIdenticalPairs(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: numIdenticalPairs({nums}) = {result}")
