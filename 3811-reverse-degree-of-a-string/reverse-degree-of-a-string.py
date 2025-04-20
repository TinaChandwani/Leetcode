class Solution:
    def reverseDegree(self, s: str) -> int:
        char_map = {char: 26 - index for index,char in enumerate (string.ascii_lowercase)}
        return sum((i+1) * char_map[c] for i,c in enumerate(s))
        