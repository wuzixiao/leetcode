class Solution:
    def isValid(self, s: str) -> bool:
        sta = []
        for v in s:
            if '([{'.find(v) >= 0:
                sta.append(v)
            else:
                if len(sta) is 0:
                    return False
                if v is ')' and sta[-1] is not '(':
                    return False
                if v is ']' and sta[-1] is not '[':
                    return False
                if v is '}' and sta[-1] is not '{':
                    return False
                
                sta.pop()

        if len(sta) is 0:
            return True
        
        return False

s = Solution()
print(s.isValid("({[]})"))
print(s.isValid("({[]}"))
print(s.isValid("({[})"))

