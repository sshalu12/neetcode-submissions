class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)          # required counts
        missing = len(t)           # total chars still missing
        left = 0
        best_start = 0
        best_len = float("inf")

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                left_char = s[left]
                need[left_char] += 1
                if need[left_char] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]