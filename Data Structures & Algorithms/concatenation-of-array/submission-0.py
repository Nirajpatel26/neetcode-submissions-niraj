class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res =[]
        n=2*len(nums)
        i=0
        while n>0:
            if i == len(nums):
                i=0
            res.append(nums[i])
            i+=1
            n-=1
        return res