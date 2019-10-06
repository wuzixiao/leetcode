class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
    def isAnagram2(self, s: str, t: str) -> bool:
        sDict, tDict = {}, {}
        for c in s:
            sDict[c] = sDict.get(c,0) + 1
        for c in t:
            tDict[c] = tDict.get(c,0) + 1

        return sDict == tDict

    def isAnagram3(self, s: str, t: str) -> bool:
        slist, tlist = [0]*26, [0]*26
        for c in s:
            slist[ord(c)-ord('a')] += 1
        for c in t:
            tlist[ord(c)-ord('a')] += 1
        
        return slist == tlist


print(Solution().isAnagram('abc', 'cba'))
print(Solution().isAnagram2('abc', 'cba'))
print(Solution().isAnagram3('abc', 'cba'))
print(Solution().isAnagram2('abc', ''))
print(Solution().isAnagram3('abc', ''))