class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = len(nums)
        seen = {}

        for i in range(l):
            
            curr = nums[i]
            diff = target - curr

            if diff in seen:
                return [seen[diff], i]
            else:
                seen[curr] = i
        