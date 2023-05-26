class Solution(object):
    def mergeAlternately(self, word1, word2):
        merge = ""
        len1 = len(word1)
        len2 = len(word2)

        max_length = max(len1,len2)

        for i in range(max_length):
            if i < len1:
                merge += word1[i]
            if i < len2:
                merge += word2[i]

        return merge

            