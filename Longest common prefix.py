def longestCommonPrefix(self, strs: list[str]) -> str:
        lcp = str()
        min_range = 999999
        for s in strs:
            l = len(s)
            if l < min_range:
                min_range = l
        
        for i in range(min_range):
            if strs[0][i] == strs[1][i] == strs[2][i]:
                lcp += strs[0][i]
            else:
                break
        return lcp

strs = ["flower","flow","flight"]
lcs = longestCommonPrefix(strs)
print(lcs)
