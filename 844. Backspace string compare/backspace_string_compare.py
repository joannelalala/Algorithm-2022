class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # for this problem, we could look at the strings backwards; if encoutering a "#", the next lowercase char will be skipped.
        # and we initialize two variables to store the skipping counts

        i = len(s) - 1
        j = len(t) - 1

        backS = backT = 0 # variables to store the skipping counts

        while True: # both s and t are not None
            while i >= 0 and (backS != 0 or s[i] == '#'):
                backS += 1 if s[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT != 0 or t[j] == '#'):
                backT += 1 if t[j] == '#' else -1
                j -= 1

            if not (i >= 0 and j >= 0 and s[i] == t[j]): # if not the abve two cases, both i and j are -1
                return i == j == -1 

            i , j = i - 1, j - 1

