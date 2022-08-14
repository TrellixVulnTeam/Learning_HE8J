from ast import Param
from collections import deque
class ParenthesesString:
    def __init__ (self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount


    def generateValidParentheses(num):
        result = []
        queue = deque()

        queue.append(ParenthesesString("",0,0))
        while queue:
            current = queue.popleft()
            if current.openCount == num and current.closeCount == num:
                result.append(current)
            
            else:
                if current.openCount <= num:
                    queue.append(ParenthesesString(current.str + "(", current.openCount + 1, current.closeCount))

                if current.closeCount < current.openCount:
                    queue.append(ParenthesesString(current.str + ")", current.openCount, current.closeCount + 1))
        
        return result

print([x.str for x in ParenthesesString.generateValidParentheses(3)])