"""Problem 4: How Many Numbers Are Smaller Than the Current Number
LeetCode Problem #1365
Difficulty: Easy

Given the array nums, for each nums[i] find out how many numbers in the array
are smaller than it. That is, for each nums[i] you have to count the number of
valid j's such that j != i and nums[j] < nums[i].

Example 1:
    Input: nums = [8,1,2,2,3]
    Output: [4,0,1,1,3]

Example 2:
    Input: nums = [6,5,4,8]
    Output: [2,1,0,3]
"""

from typing import List


class Solution:
    """Solution to How Many Numbers Are Smaller Than Current Number."""
    
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        For each number, count how many numbers are smaller than it.
        
        Time Complexity: O(n^2)
        Space Complexity: O(n) for output array
        
        Args:
            nums: Array of integers
            
        Returns:
            Array where result[i] = count of numbers smaller than nums[i]
        """
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result
    
    def smallerNumbersThanCurrentOptimized(self, nums: List[int]) -> List[int]:
        """
        Optimized approach using sorting.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        
        Args:
            nums: Array of integers
            
        Returns:
            Array where result[i] = count of numbers smaller than nums[i]
        """
        # Create pairs of (value, original_index)
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        # Sort by value
        indexed_nums.sort()
        
        result = [0] * len(nums)
        for rank, (num, original_index) in enumerate(indexed_nums):
            result[original_index] = rank
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8], [2, 1, 0, 3]),
    ]
    
    for nums, expected in test_cases:
        result = solution.smallerNumbersThanCurrent(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: smallerNumbersThanCurrent({nums}) = {result}")
