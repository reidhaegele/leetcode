class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        output = []
        for i in range(k):
            m = 0
            num_max = 0

            for c in count:
                if c not in output:
                    if count[c] > m:
                        m = count[c]
                        num_max = c
            output.append(num_max)
        return output
