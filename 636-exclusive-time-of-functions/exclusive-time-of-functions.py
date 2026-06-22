class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        curr_time = 0
        prev_time = 0
        res = [0] * n

        for i in range(len(logs)):
            log = logs[i].split(':')
            log_id = int(log[0])
            time = int(log[2])
            if log[1] == "start":
                if stack:
                    curr_time = time
                    diff = curr_time - prev_time
                    res[stack[-1]] += diff
                    prev_time = curr_time
                stack.append(log_id)
            else:
                i = stack.pop()
                curr_time = time + 1
                diff = curr_time - prev_time
                res[i] += diff
                prev_time = curr_time
            
            print(res)
    
        return res