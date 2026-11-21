class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(n^2) would be to iterate over each element and exclude it 
        # and use remaining elements to multiply

        n = len(nums)

        left = [1] * n
        right = [1] * n
        output = [0] * n

        for i in range(n):
            if i == 0:
                continue
            else:
                left[i] = left[i - 1] * nums[i - 1]
                right[n - i - 1] = right[n - i] * nums[n - i] 

        for i in range(n):
            output[i] = left[i] * right[i]

        return output