"""
# Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

    Input: s = "IceCreAm"
    Output: "AceCreIm"
    Explanation:
        - The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

    Input: s = "leetcode"
    Output: "leotcede"

"""


def reverse_vowels_in_string(s):
    vowels = set("aeiouAEIOU")
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] not in vowels:
            left += 1

        elif s[right] not in vowels:
            right -= 1

        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)


if __name__ == "__main__":
    string = "leetcode"
    print(f"Initial string: {string}")

    result = reverse_vowels_in_string(string)
    print(f"Result string: {result}")
