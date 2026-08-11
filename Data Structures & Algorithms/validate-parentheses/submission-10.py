class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            # init correct pop to be used in comparison
            correctPop = None
            if i == ")":
                correctPop = "("
            elif i == "]":
                correctPop = "["
            else:
                correctPop = "{"

            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif bool(stack) and stack.pop() == correctPop:
                continue
            else:
                return False
        if bool(stack):
            return False
        return True