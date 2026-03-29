class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [i.lower() for i in s if i.isalnum()] 
        left= 0
        right=len(a)-1
        while left < right:
            if a[left] == a[right]:
                left +=1
                right -=1
            else: 
                return False

        return True 


        
        