from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stk =[]

        mapping ={")":"(","}":"{","]":"["}

        for char in s:
            
            if char in mapping:
                top= stk.pop() if stk else"#"

                if mapping[char] != top:
                    return False
            else:
                stk.append(char)

        return not stk 

        