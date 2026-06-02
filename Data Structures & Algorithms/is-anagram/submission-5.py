class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        if set(s) != set(t):
            return False

        sc = {}
        tc = {}

        for ch in s:
            if ch in sc.keys():
                sc[ch] = sc[ch] + 1
            else:
                sc[ch] = 1

        for ch in t:
            if ch in tc.keys():
                tc[ch] = tc[ch] + 1
            else:
                tc[ch] = 1

        for key, value in tc.items():
            if sc[key] != value:
                return False
        
        return True
            