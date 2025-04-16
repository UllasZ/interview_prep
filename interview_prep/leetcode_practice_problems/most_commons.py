"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

 would have it's logo with the letters .

Input Format

A single line of input containing the string .

Constraints

 has at least  distinct characters
Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order
"""

import collections

s = "aabbbccde"

# Split input string into list of characters
character_list = list(s)

# Count occurrence of each character
from collections import Counter

character_count = Counter(character_list)
character_count_list = list(character_count.items())

# Sort by character count first (descending) and then alphabetically (ascending) if counts are same
sorted_char_count = sorted(character_count_list, key=lambda x: (-x[1], x[0]))
top_three_characters = sorted_char_count[:3]

# Print top three characters with their corresponding occurrence count
for char, count in top_three_characters:
    print(char, count)
