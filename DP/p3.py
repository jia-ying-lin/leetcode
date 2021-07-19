class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        sub_s = []
        max_l = 0
        for c in s:
            if c in sub_s:
                max_l = len(sub_s) if len(sub_s) > max_l else max_l
                i = sub_s.index(c)
                sub_s = sub_s[i+1:]
                sub_s.append(c)
            else:
                sub_s.append(c)
        max_l = len(sub_s) if len(sub_s) > max_l else max_l
        return max_l