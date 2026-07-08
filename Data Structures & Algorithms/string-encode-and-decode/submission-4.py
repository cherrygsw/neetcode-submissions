class Solution:
    def encode(self, strs: List[str]) -> str:
        result = "" # make list of strings into a single string
        for s in strs:
            result += str(len(s)) + "#" + s # the start of each string in the list will have the length, a differentiator, and the string. this will combine all strings in the list with thier length and the differentiator in front of it (s)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 # tell what position at in input string

        while i < len(s):
            j = i # 2nd pointer
            while s[j] != "#": # as long as the character j is pointing to is not the differentiatior, meaning we are at integer
                j += 1 # keep incrementing till we get pound
            length = int(s[i:j]) # the value of j is until we get to next differentiator, showing us length is how many character we have to read after j to get every char of string
            result.append(s[j+1:j+1+length])
            i = j+1+length
        return result