class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c={}
        l=0
        max_len=0
        for r in range(len(s)):
            if s[r] in c and c [s[r]] >=l:
                l=c[s[r]]+1
            c[s[r]] =r
            max_len=max(max_len,r-l+1)
        return max_len
