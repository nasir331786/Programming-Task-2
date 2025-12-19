"""Problem 1: Defanging an IP Address
LeetCode Problem #1108
Difficulty: Easy

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"

Example 2:
    Input: address = "255.100.50.0"
    Output: "255[.]100[.]50[.]0"
"""

from typing import Optional


class Solution:
    """Solution to Defanging an IP Address problem."""
    
    def defangIPaddr(self, address: str) -> str:
        """
        Replace every period with "[.]"
        
        Time Complexity: O(n) where n is the length of the address
        Space Complexity: O(n) for the output string
        
        Args:
            address: A valid IPv4 address string
            
        Returns:
            Defanged version of the IP address
        """
        return address.replace(".", "[.]")


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("1.1.1.1", "1[.]1[.]1[.]1"),
        ("255.100.50.0", "255[.]100[.]50[.]0"),
    ]
    
    for address, expected in test_cases:
        result = solution.defangIPaddr(address)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: defangIPaddr('{address}') = '{result}'")
