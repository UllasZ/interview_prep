"""
Write a Python function to find the first non-repeating character in a string. Return None if every character repeats.
"""

def find_first_non_repeating_character(string):

    counter = {}

    for i in string:
        counter[i] = counter.get(i, 0) + 1

    for k, v in counter.items():
        if v == 1:
            return k
    return None


s = "helloehjjcel"
print(find_first_non_repeating_character(s))