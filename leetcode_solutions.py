# LeetCode Solutions - Programming Task 2
# Innomatics Research Labs
# Author: nasir331786
# Date: 2025-12-19

from typing import List

# Problem 1: Defanging an IP Address
class Solution1:
    """1108. Defanging an IP Address
    Given a valid (IPv4) IP address, return a defanged version of that IP address.
    """
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


# Problem 2: Find Numbers with Even Number of Digits
class Solution2:
    """1295. Find Numbers with Even Number of Digits
    Given an array nums of integers, return how many of them contain an even number of digits.
    """
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(abs(num))) % 2 == 0:
                count += 1
        return count


# Problem 3: Number of Good Pairs
class Solution3:
    """1512. Number of Good Pairs
    Given an array of integers nums, return the number of good pairs.
    A pair (i, j) is called good if nums[i] == nums[j] and i < j.
    """
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count


# Problem 4: How Many Numbers Are Smaller Than the Current Number
class Solution4:
    """1365. How Many Numbers Are Smaller Than the Current Number
    Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
    """
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result


# Problem 5: Subtract the Product and Sum of Digits of an Integer
class Solution5:
    """1281. Subtract the Product and Sum of Digits of an Integer
    Given an integer number n, return the difference between the product of its digits and the sum of its digits.
    """
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        for digit in str(n):
            product *= int(digit)
            total += int(digit)
        return product - total


# Problem 6: XOR Operation in an Array
class Solution6:
    """1486. XOR Operation in an Array
    Given an integer n and an integer start.
    Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
    Return the bitwise XOR of all elements of nums.
    """
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= (start + 2 * i)
        return result


# Test Cases
if __name__ == "__main__":
    # Test Problem 1
    sol1 = Solution1()
    assert sol1.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    print("Problem 1 passed!")

    # Test Problem 2
    sol2 = Solution2()
    assert sol2.findNumbers([12, 345, 2, 6, 7896]) == 2
    print("Problem 2 passed!")

    # Test Problem 3
    sol3 = Solution3()
    assert sol3.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
    print("Problem 3 passed!")

    # Test Problem 4
    sol4 = Solution4()
    assert sol4.smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
    print("Problem 4 passed!")

    # Test Problem 5
    sol5 = Solution5()
    assert sol5.subtractProductAndSum(234) == 15
    print("Problem 5 passed!")

    # Test Problem 6
    sol6 = Solution6()
    assert sol6.xorOperation(5, 0) == 8
    print("Problem 6 passed!")

    print("All tests passed!")
