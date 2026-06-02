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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        for i in range(len(strs)):
            ans1 = []
            current = strs[i]
            ans1.append(current)
            for strss in strs[0:i] + strs[i+1:]:
                if self.isAnagram(current, strss):
                    ans1.append(strss)
            ans1.sort()
            if ans1 in ans:
                continue
            ans.append(ans1)

        return ans

        