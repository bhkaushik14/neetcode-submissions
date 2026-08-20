class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        longest = 0
        freq = {}

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            window_size = r - l + 1
            most_freq = max(freq.items(), key= lambda x: x[1])[1]

            if window_size - most_freq <= k:
                if window_size > longest:
                    longest = window_size
            else:
                freq[s[l]] -= 1
                l += 1
            r += 1

        return longest