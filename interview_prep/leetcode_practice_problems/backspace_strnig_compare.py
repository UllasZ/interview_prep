"""
# Backspace String Compare

- Given two strings s and t, return true if they are equal when both are typed into empty text editors.
- '#' means a backspace character.
- Note that after backspacing an empty text, the text will continue empty.

Example 1:
    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".

Example 2:
    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".

Example 3:
    Input: s = "a#c", t = "b"
    Output: false
    Explanation: s becomes "c" while t becomes "b".
"""


def backspace_compare(s, t):
    s1, t1 = [], []
    for i in s:
        if i == "#":
            if s1:
                s1.pop()
            else:
                continue
        else:
            s1.append(i)

    for i in t:
        if i == "#":
            if t1:
                t1.pop()
            else:
                continue
        else:
            t1.append(i)

    print(s1, t1)
    return s1 == t1


# str1 = "ab#c"
# str2 = "ad#c"

str1 = "ab##"
str2 = "c#d#"

res = backspace_compare(str1, str2)
print(res)
