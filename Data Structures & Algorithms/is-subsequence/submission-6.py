class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            idx = t.find(c)
            t = t[idx+1:len(t)] #next scan should only consider remaining part of string
            print(t)
            if idx == -1 :
                return False

        return True