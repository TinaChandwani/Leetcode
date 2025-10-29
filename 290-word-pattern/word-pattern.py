class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        n = len(pattern)
        if n != len(arr):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(n):
            if pattern[i] not in dict1:
                dict1[pattern[i]] = arr[i]
            else:
                if dict1[pattern[i]] != arr[i]:
                    return False
                dict1[pattern[i]] = arr[i]
            if arr[i] not in dict2:
                dict2[arr[i]] = pattern[i]
            else:
                if pattern[i] != dict2[arr[i]]:
                    return False
                dict2[arr[i]] = pattern[i]
        return True
           

        print(f'dict1 {dict1}')
        print(f'dict2 {dict2}')
        # if len(dict1) != len(dict2):
        #     return False
        # for key, val in dict1.items():
        #     if val in dict2:
        #         if dict2[val] == key:
        #             continue
        #         else:
        #             return False
        #     else:
        #         return False
        # return True



            
            