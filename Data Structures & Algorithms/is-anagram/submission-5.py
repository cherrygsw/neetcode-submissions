class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t): # strings are diff length automatically cant be anagrams
            return False
        
        countS = {} # building a dict where each key is a letter, abd value is how many times the letter shows up
        countT = {}

        for i in range(len(s)): # length of word
            countS[s[i]] = 1 + countS.get(s[i],0) # find the value of this letter in this dict, if not, treat it as 0 + 1
            countT[t[i]] = 1 + countT.get(t[i],0)

        for c in countS: # loops thru every distinct letter seen in s
            if countS[c] != countT.get(c,0): # if value of how many times the letter appears is not the same, if not appeared returns 0 instead of crashing
                return False
        return True
            