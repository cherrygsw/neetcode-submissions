class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # if letter has not been accounted for then the default value is 0
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
        
        return True

# can use counter function like: return Counter(s) == Counter(t)