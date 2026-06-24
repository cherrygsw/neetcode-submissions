class Solution:
    def encode(self, strs: List[str]) -> str:
        # Encode each string as "<length>#<string>"
        # Example: ["neet","code"] -> "4#neet4#code"
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the position of delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # length of the next string
            # Extract the substring of that length after '#'
            word = s[j+1 : j+1+length]
            res.append(word)
            # Move i past this encoded word
            i = j + 1 + length
        return res
