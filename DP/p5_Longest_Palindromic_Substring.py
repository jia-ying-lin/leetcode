# Brute Force
# Time Complexity: O(n^3)
# Space Complexity: O(n)
# Ref:
# https://algorithm.yuanbin.me/zh-tw/string/longest_palindromic_substring.html
class Solution:
    def longestPalindrome(self, s: str) -> str:          
        max_s = s[0]
        max_l = 1
        for i in range(len(s)-1):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    if j-i > max_l:
                        max_l = j-i
                        max_s = s[i:j]
        return max_s
# DP
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:  
        if len(s) == 1:
            return s
        max_len = 1
        max_start = 0
        max_str = s[0]
        dp = [[0]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1] == 1:  
                        dp[i][j] = 1
                        if j-i+1 > max_len:
                            max_start = i
                            max_len = j-i+1
        return s[max_start:max_start+max_len]

# Manacher's Algorithm
# Time Complexity: O(n)
# Ref:
# https://medium.com/hoskiss-stand/manacher-299cf75db97e 
# http://manacher-viz.s3-website-us-east-1.amazonaws.com/#/
# https://www.youtube.com/watch?v=YVZttWzvyw8
class Solution:
    def longestPalindrome(self, s: str) -> str:  
        if len(s) == 1:
            return s
        
        l = ['_']*(len(s)*2+1)
        lps = [0]*(len(s)*2+1)
        for i in range(len(s)):
            l[i+(i+1)] = s[i]
        
        max_len = 1
        max_c = 1
        L = 0
        R = 0
        c = 0
        r = 1
        for i in range(1, len(l)):
            if i >= R:
                c = i
                r = 1
                while i-r >= 0 and i+r < len(l) and l[i-r] == l[i+r]:
                    L = i-r
                    R = i+r
                    if r > max_len:
                        max_len = r
                        max_c = i
                    lps[i] = r
                    r += 1
            else:
                mirro_i = c*2-i
                if mirro_i-lps[mirro_i] > L:
                    lps[i] = lps[mirro_i]
                else:
                    r = min(R - i, lps[mirro_i])
                    while i-r >= 0 and i+r < len(l) and l[i-r] == l[i+r]:
                        L = i-r
                        R = i+r
                        if r > max_len:
                            max_len = r
                            max_c = i
                        lps[i] = r
                        r += 1
        return ''.join(l[max_c-max_len:max_c+max_len+1]).replace("_", "")