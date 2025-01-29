class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Dictionary to store number and its index

        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement
            if complement in num_map:
                return [num_map[complement], i]  # Return the indices
            num_map[num] = i  # Store the current number and its index
        