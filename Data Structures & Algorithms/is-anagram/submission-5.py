from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)== len(t) and set(s) == set(t) and Counter(s)==Counter(t):
            return True
        else:
            return False