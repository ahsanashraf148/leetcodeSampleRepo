"""
Traverse through the list, add extraCandies compare it to the max, if greater or equal than set that index true in result list.


Difficulty Level: Easy
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candies = max(candies)
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        return result

