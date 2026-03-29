class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        my_set=set()
        n=len(s)
        
        for r in range(n):
            while s[r] in my_set:
                my_set.remove(s[l])
                l +=1
            
            w= (r-l)+1
            longest = max(longest,w)
            my_set.add(s[r])

        return longest


        