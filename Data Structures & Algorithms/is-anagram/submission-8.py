class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t) and len(s) == len(t):
            return True 
        else: 
            return False