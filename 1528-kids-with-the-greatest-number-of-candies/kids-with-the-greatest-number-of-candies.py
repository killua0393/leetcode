class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        l=[]
        for i in candies:
            if(i+extraCandies>=maxi):
                l.append(True)
            else:
                l.append(False)
        return l

        