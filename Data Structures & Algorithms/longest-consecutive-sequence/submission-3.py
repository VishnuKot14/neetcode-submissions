class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsHash = set(nums)
        lcs = 0

        for num in numsHash:
            if (num - 1) not in numsHash:
                length = 1
                while (num + length) in numsHash:
                    length += 1
                lcs = max(length, lcs)
        
        return lcs

        
        
