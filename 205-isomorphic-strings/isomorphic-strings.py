class Solution:
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        map_s_t={}
        map_t_s={}
        for a, b in zip(s, t):
            if a in map_s_t and map_s_t[a]!=b:
                return False
            if b in map_t_s and map_t_s[b]!=a:
                return False
            map_s_t[a]=b
            map_t_s[b]=a
        return True