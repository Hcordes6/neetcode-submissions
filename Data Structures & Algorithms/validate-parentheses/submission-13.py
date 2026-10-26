class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {")": "(", "}": "{", "]": "["}

        for i in s:
            print(i)
            print(stack)
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif stack and stack[-1] == d.get(i):
                stack.pop()
                print("success")
                continue
            else:
                return False
        if not stack:
            return True 
        else:
            return False