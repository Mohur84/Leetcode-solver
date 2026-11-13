class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed=[]
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            parsed.append((name, int(time), int(amount), city, i))
        invalid=set()
        for i in range(len(parsed)):
            name1, time1, amount1, city1, _=parsed[i]
            if amount1>1000:
                invalid.add(i)
            for j in range(i+1, len(parsed)):
                name2, time2, amount2, city2, _=parsed[j]
                if (name1==name2 and abs(time1-time2)<=60 and city1!=city2):
                    invalid.add(i)
                    invalid.add(j)
        return[
            transactions[i]
            for i in range(len(transactions))
            if i in invalid
        ]