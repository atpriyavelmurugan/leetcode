class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        k = [-1] 
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                k.append(i)
            else:
                k.pop()
                if not k:
                    k.append(i)
                else:
                    max_len = max(max_len, i - k[-1])

        return max_len

sol = Solution()
print(sol.longestValidParentheses("(()")) 
