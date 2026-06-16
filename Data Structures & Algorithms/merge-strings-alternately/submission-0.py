class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1,w2 = 0, 0
        word3 =[]
        while w1 < len(word1) or w2 < len(word2):
            if w1 < len(word1):
                word3.append(word1[w1])
            if w2 < len(word2):
                word3.append(word2[w2])
            w1 +=1
            w2 +=1
        return "".join(word3)
