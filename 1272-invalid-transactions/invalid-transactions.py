class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tDict = defaultdict(list)
        output = set()
        for i in range(len(transactions)):
            name,time,amt,city = transactions[i].split(',')
            tDict[name].append((int(time),int(amt),city,i))
        print(f' tDict {tDict}')
        for curr_idx,curr_t in enumerate(transactions):
            curr_name,curr_time,curr_amt,curr_city = transactions[curr_idx].split(',')
            curr_amt = int(curr_amt)
            curr_time = int(curr_time)
            if curr_amt > 1000:
                output.add(curr_idx)
                continue
            else:
                for val in tDict[curr_name]:
                    next_time,next_amt,next_city,txn_id = val
                    if txn_id != curr_idx and abs(next_time - curr_time) <= 60 and next_city != curr_city:
                        output.add(curr_idx)
                        break
        
        return [transactions[i] for i in output]



