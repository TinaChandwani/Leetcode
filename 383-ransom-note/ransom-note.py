class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = []

        for i in magazine:
            store.append(i)
        
        for j in ransomNote:
            if j in store:
                store.remove(j)
            else:
                return False
        return True