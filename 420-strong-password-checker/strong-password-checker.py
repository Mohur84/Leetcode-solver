class Solution:
    def strongPasswordChecker(self, password):
        n=len(password)
        missing=0
        if not any(c.islower() for c in password):
            missing+=1
        if not any(c.isupper() for c in password):
            missing+=1
        if not any(c.isdigit() for c in password):
            missing+=1
        runs=[]
        i=0
        while i<n:
            j=i
            while j<n and password[j]==password[i]:
                j+=1
            length=j-i
            if length>=3:
                runs.append(length)
            i=j
        if n<6:
            return max(missing, 6-n)
        replacements=sum(length//3 for length in runs)
        if n<=20:
            return max(missing, replacements)
        deletions=n-20
        remaining_deletions=deletions
        for i in range(len(runs)):
            if remaining_deletions==0:
                break
            if runs[i]%3==0:
                delete=min(remaining_deletions, 1)
                runs[i]-=delete
                remaining_deletions-=delete
        for i in range(len(runs)):
            if remaining_deletions<2:
                break
            if runs[i]%3==1:
                delete=min(remaining_deletions, runs[i]-2)
                runs[i]-=delete
                remaining_deletions-=delete
        for i in range(len(runs)):
            if remaining_deletions==0:
                break
            delete=min(remaining_deletions, runs[i]-2)
            runs[i]-=delete
            remaining_deletions-=delete
        replacements=sum(length//3 for length in runs)
        return deletions + max(missing, replacements)