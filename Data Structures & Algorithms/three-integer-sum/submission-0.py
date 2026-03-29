class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        trplets =[]
        nums.sort()

        for index,val in enumerate(nums):

            if(index > 0) and (val == nums[index-1]):
                continue

            l,r=index+1,len(nums)-1
            while l<r:

                sum= val+nums[l]+nums[r]

                if(sum == 0):
                    trplets.append([val,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                    
                elif sum > 0:
                    r -=1
                else:
                    l +=1
        return trplets
                           