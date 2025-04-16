"""
# HT: Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Explanation:
        - There is no string in strs that can be rearranged to form "bat".
        - The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
        - The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
"""


def group_anagrams(strs):

    my_dict = {}
    if len(strs) == 0:
        return [[""]]

    if len(strs) == 1:
        return [strs]

    for i in strs:
        sorted_i = "".join(sorted(i))

        if sorted_i not in my_dict:
            my_dict[sorted_i] = [i]
        else:
            my_dict[sorted_i].append(i)

    return sorted(list(my_dict.values()))


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
# arr = []
# arr = ["a"]
print(group_anagrams(arr))
