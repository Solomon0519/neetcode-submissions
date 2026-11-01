class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = {}
        array_length = len(nums)

        for i in range(array_length):
            
            curr = nums[i]

            if curr in seen:
                return True
            else:
                seen[curr] = True
        
        return False
