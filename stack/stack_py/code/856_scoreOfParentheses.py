class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack=[]
        for c in S: 
            if c=='(':
                stack.append(c)
            else:
                tc=stack[-1]
                if tc=='(':
                    stack.pop()
                    stack.append(1)
                else:
                    num=0
                    while stack[-1]!='(':
                        num+=stack.pop()
                    stack.pop()
                    stack.append(num*2)
        return sum(stack)