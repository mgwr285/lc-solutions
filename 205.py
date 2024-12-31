class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp, st = dict(), set()
        for i in range(len(s)):
            if s[i] not in mp:
                if t[i] in st:
                    return False
                mp[s[i]] = t[i]
                st.add(t[i])
            elif mp[s[i]] != t[i]:
                return False
        return True
