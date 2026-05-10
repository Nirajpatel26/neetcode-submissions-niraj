

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set()
        n = len(nums)

        if n == len(set(nums)):
            return False
        else:
            return True

        
        