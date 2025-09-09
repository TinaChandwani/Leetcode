class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        n = len(path)
        i = 0

        while i < n-1:
            if path[i] == '/':
                currS = ''
                while i+1 < n and path[i+1] != '/':
                    currS += path[i+1]
                    i += 1
                if currS != '..':
                    if len(currS) == 0 or currS == '.':
                        i += 1
                        continue
                    stack.append(currS)
                else:
                    if len(stack) != 0:
                        stack.pop()
            i += 1
        return '/' + '/'.join(stack)
        