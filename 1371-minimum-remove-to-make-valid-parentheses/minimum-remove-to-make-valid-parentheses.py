class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Using counts:
            - keeping count for open_count from left to right and
            - then count for close_count from right to left
        '''
        result = ''
        final_result = ''
        open_count = 0
        close_count = 0

        for i in s:
            if i == '(':
                open_count += 1
            elif i == ')':
                if open_count > 0:
                    open_count -= 1
                else:
                    continue
            result += i
        
        # if open_count == 0:
        #     return result
        # else:
        for j in range(len(result)-1,-1,-1):
            if result[j] == ')':
                close_count += 1
            elif result[j] == '(':
                if close_count > 0:
                    close_count -= 1
                else:
                    continue
            final_result += result[j]
                
        return final_result[::-1]

        