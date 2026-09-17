class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
                return (lambda: max((right - left + 1) for left in range(len(s)) for right in range(left, len(s)) if (right - left + 1) - max((s[left:right+1]).count(c) for c in set(s[left:right+1])) <= k))()