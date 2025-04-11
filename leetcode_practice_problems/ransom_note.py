"""
# Ransom Note
- Given two strings ransomNote and magazine,
  return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
- Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:
    Input: ransomNote = "aa",  = "aab"
    Output: true
"""


def can_construct(ransom_note, magazine):

    my_dict = {}

    for i in magazine:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1

    for i in ransom_note:
        if i in my_dict and my_dict[i] > 0:
            my_dict[i] -= 1
        else:
            return False

    return True


note = "aaa"
mag = "aab"

print(can_construct(note, mag))
