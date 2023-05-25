class Solution(object):
    def percentageLetter(self, s, letter):
        numOfLetters = len(s)
        counter = 0
        for char in s:
            if char == letter:
                counter += 1
        percent = (counter / float(numOfLetters)) * 100
        whole_percent = int(percent)
        return whole_percent
