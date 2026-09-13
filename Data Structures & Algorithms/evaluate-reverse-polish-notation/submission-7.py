class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+','*','-','/'}

        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                first= int(stack.pop())
                secound =int(stack.pop())
                if i == '+':
                    res= first+secound
                    stack.append(res)
                elif i =='*':
                    res =first * secound
                    stack.append(res)
                elif i =='-':
                    res = secound - first
                    stack.append(res)
                else:
                    res = int(float(secound/first))
                    stack.append(res)
        
        return stack.pop()
            

        
