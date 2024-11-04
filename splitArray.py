class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        
        #Easier way counter = Counter(nums)
        freq = {}

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]= 1

        for f in freq.values():
            if f > 2:
                return False
        return True