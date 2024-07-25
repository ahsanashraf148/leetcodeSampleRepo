"""
Hash Map Initialization: Start by creating an empty hash map (dictionary) to store the numbers and their corresponding indices as you iterate through the array.

Iterate Through the Array: As you iterate through each element in the array, calculate the complement of the current element by subtracting it from the target.

Check for Complement: For each element, check if the complement (target - current element) exists in the hash map.

If it does, you have found the two indices that sum up to the target. Return these indices.
If it doesn't, add the current element and its index to the hash map.
Continue Until Solution Found: Continue this process until you find the two indices.

Why This Works:
Efficiency: Using a hash map allows you to check for the existence of the complement in constant time 
O(1).
Single Pass: You can find the solution in a single pass through the array, making the time complexity 
O(n).
Space Complexity: The space complexity is 
O(n) due to storing the elements and indices in the hash map.


Difficulty Level: Easy
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for index, num in enumerate(nums):
            # Calculate the complement that we need to find
            complement = target - num
            
            # If the complement exists in the hash map, return the sol
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Otherwise, store the index of the current number
            num_to_index[num] = index

