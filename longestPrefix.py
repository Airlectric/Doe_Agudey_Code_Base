class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        string_comparer = min(strs, key=len)

        for i, letter in enumerate(string_comparer):
            for word in strs:
                if word[i] != letter:
                   return string_comparer[:i]

        return string_comparer
            
