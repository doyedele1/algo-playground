class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_map = {}

        for i in range(n):
            diff = target - nums[i]
            num = nums[i]
            if diff in nums_map:
                return [nums_map[diff], i]
            nums_map[num] = i
                
            