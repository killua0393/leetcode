class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maps={}
        for i in nums:
            if i not in maps:
                maps[i]=1
            else:
                maps[i]=maps[i]+1
        for i in maps:
            if maps[i]==1:
                return i


        