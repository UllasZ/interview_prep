"""
# HT: First Non-Repeating Character ( ** Interview Question)

- You have been given a string of lowercase letters.
- Write a function called first_non_repeating_char(string) that finds the first non-repeating character
  in the given string using a hash table (dictionary).
- If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character
that appears only once in the string. Similarly, if the input string is "hello",
the function should return "h" because "h" is the first non-repeating character in the string.
"""


def first_non_repeating_char(string):

    my_dict = {}
    result = None

    for i in string:
        my_dict[i] = my_dict.get(i, 0) + 1

    for key, count in my_dict.items():
        if count == 1:
            result = key
            break

    return result


print(first_non_repeating_char("leetcode"))

print(first_non_repeating_char("hello"))

print(first_non_repeating_char("aabbcc"))


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
