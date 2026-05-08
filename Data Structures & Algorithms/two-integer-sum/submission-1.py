class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_map = {}

        for i in range(n):
            diff = target - nums[i]
            num = nums[i]
            if diff not in nums_map:
                nums_map[num] = i
            else:
                return [nums_map[diff], i]
            