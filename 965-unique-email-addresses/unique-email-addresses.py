class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique=set()
        for email in emails:
            local, domain=email.split('@')
            local=local.split('+')[0]
            local=local.replace('.','')
            normalized=local+'@'+domain
            unique.add(normalized)
        return len(unique)