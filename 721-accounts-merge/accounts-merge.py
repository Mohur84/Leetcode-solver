class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n=len(accounts)
        parent=list(range(n))
        rank=[0]*n
        email_to_id={}
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x, y):
            root_x=find(x)
            root_y=find(y)
            if root_x==root_y:
                return
            if rank[root_x]<rank[root_y]:
                parent[root_x]=root_y
            elif rank[root_x]>rank[root_y]:
                parent[root_y]=root_x
            else:
                parent[root_y]=root_x
                rank[root_x]+=1
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    union(i, email_to_id[email])
                else:
                    email_to_id[email]=i
        groups=defaultdict(list)
        for email, account_id in email_to_id.items():
            root=find(account_id)
            groups[root].append(email)
        result=[]
        for root, emails in groups.items():
            result.append([accounts[root][0]]+sorted(emails))
        return result