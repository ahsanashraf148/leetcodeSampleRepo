"""
Merge Function: This helper function takes two sorted arrays (left and right) and merges them into a single sorted array. It uses two pointers to keep track of the current index in each array and appends the smaller element to the sorted_array.

Merge Sort Function: This recursive function divides the array into two halves until the base case (a single element) is reached. It then merges the sorted halves by calling the merge function.

Sort Array Function: This function initializes the sorting process by calling merge_sort on the input array nums.

Complexity Analysis:
Time Complexity: 
O(nlogn) because the array is repeatedly split into halves (logarithmic splits) and each split array is processed linearly (n).
Space Complexity: 
O(n) due to the additional space used for the temporary arrays created during the merging process. This can be optimized with in-place modifications but would complicate the implementation.

For same time complexity and O(1) space complexity use heap sort



Difficulty Level: Medium
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left: List[int], right: List[int]) -> List[int]:
            sorted_arr = []
            i = j = 0
            while i < len(left) and j < len(right):
                if(left[i] < right[j]):
                    sorted_arr.append(left[i])
                    i+=1
                else:
                    sorted_arr.append(right[j])
                    j+=1
            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])
            return sorted_arr

        def merge_sort(arr: List[int]) -> List[int]:
            n = len(arr)
            if n <= 1:
                return arr
            mid = n // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        return merge_sort(nums)
        
        
