class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_dict = {}

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, count in count_dict.items():
            buckets[count].append(num)

        k_most_frequent = []
        count = 0

        for i in range(len(buckets) -1, -1, -1):
            if not buckets[i]:
                continue
            else:
                bucket_size = len(buckets[i])
                count += bucket_size
                k_most_frequent.extend(buckets[i])

                if count >= k:
                    return k_most_frequent
        
        return
