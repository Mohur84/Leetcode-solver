class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain=s.lower().split('@')
            return name[0]+'*****'+name[-1]+'@'+domain
        digits=''.join(ch for ch in s if ch.isdigit())
        local='***-***-'+digits[-4:]
        country_length=len(digits)-10
        if country_length==0:
            return local
        return '+'+'*'*country_length+'-'+local