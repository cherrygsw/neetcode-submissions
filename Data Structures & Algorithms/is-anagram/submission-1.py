class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t): # check if the words have the same amount of characters
            return False # if they don't have an equal amount of letters then return false
        
        countS = {} # set a hashMap for the first word
        countT = {} # set a hashMap for the second word

        for i in range(len(s)): # check each character depedning on the length of the word
            countS[s[i]] = 1 + countS.get(s[i],0) # move on to the next index for first word
            countT[t[i]] = 1 + countT.get(t[i],0) # move on to the next index for the second word
        for c in countS: # check for each value of each letter in each word
            if countS[c] != countT.get(c,0): # if they don't have the same amount
                return False # return false
        return True