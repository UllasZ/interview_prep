"""
# 2. Group Anagrams
Problem: Group strings that are anagrams of each other.
Input: ["eat","tea","tan","ate","nat","bat"] → Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
Constraints: Use sorted word as hash key for grouping.
"""

def group_anagrams(arr):

    anagrams = {}

    for word in arr:
        sorted_word = "".join(sorted(word))

        if sorted_word not in anagrams:
            anagrams[sorted_word] = []

        anagrams[sorted_word].append(word)

    return list(anagrams.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))