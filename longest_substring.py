# SOLVED

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        temp = {}
        maxLen = 0
        currentLen = 0
        firstCharIndex = 0
        for i, c in enumerate(s):
            x = temp.get(ord(c))
            if x == None:
                temp[ord(c)] = i
                currentLen += 1
            else:
                if x >= firstCharIndex:
                    firstCharIndex = x + 1
                    currentLen = (i - firstCharIndex) + 1
                else:
                    currentLen += 1
            temp[ord(c)] = i
            if currentLen > maxLen:
                maxLen = currentLen
        return maxLen

res = Solution().lengthOfLongestSubstring("bbtablud")
print(res)