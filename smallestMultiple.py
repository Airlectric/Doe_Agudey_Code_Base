class Solution(object):
    def smallestEvenMultiple(self, n):
        if n%2 == 1:
            num = n * 2
            return num
        else:
            return n
