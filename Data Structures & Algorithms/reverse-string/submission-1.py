class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,n=0,len(s)-1
        while i<n:
            s[i],s[n] = s[n],s[i]
            i+=1
            n-=1
        