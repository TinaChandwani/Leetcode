class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        main_dict = defaultdict(int)
        first_word = words[0]
        n = len(words)

        for i in first_word:
            main_dict[i] += 1
        
        for i in range(1,n):
            temp_dict = defaultdict(int)
            for j in words[i]:
                temp_dict[j] += 1
        
            keys_to_remove = []
            for char in main_dict:
                if char in temp_dict:
                    main_dict[char] = min(main_dict[char],temp_dict[char])
                else:
                    keys_to_remove.append(char)
        
            for k in keys_to_remove:
                del main_dict[k]

        result = []
        for char,count in main_dict.items():
            result.extend([char] * count)
        
        return result
