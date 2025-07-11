class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        space = " "
        count = 0
        for i in s[::-1]:
            print(f'i. {i}')
            if i != space:
                count += 1
            else:
                return count
        return count