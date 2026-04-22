class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen ={}
        best =0
        left =0
        for right, ch in enumerate(s):
            if ch in last_seen:
                left = max(last_seen[ch]+1, left)
            last_seen[ch] = right
            best = max(best, right-left+1)
        return best