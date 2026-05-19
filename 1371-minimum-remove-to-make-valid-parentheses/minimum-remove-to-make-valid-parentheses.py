class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ''
        final_res = ''
        oc = 0
        cc = 0

        for i in s:
            if i == '(':
                oc += 1
            elif i == ')':
                if oc > 0:
                    oc -= 1
                else:
                    continue
            res += i
        
        for j in range(len(res)-1,-1,-1):
            if res[j] == ')':
                cc += 1
            elif res[j] == '(':
                if cc > 0:
                    cc -= 1
                else:
                    continue
            final_res += res[j]
        
        return final_res[::-1]