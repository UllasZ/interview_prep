"""
# 3. Longest Substring Without Repeating Characters
Problem: Return the length of the longest substring without repeating characters.
Input: "abcabcbb" → Output: 3 ("abc")
Constraints: Use sliding window + set/map for O(n) time.
"""

def longest_substring(string):
    print(string)
    left, start, max_len, seen = 0, 0, 0, set()

    for right in range(len(string)):

        while string[right] in seen:
            seen.remove(string[left])
            left += 1

        seen.add(string[right])

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    longest = string[start: start+ max_len]
    return max_len, longest


print(longest_substring('abcabcbb'))
