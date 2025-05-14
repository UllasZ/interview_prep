def fib_upto_n(n):
    fib = [0, 1]

    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])

    print(fib)

fib_upto_n(23)

def palindrome(s):
    return s == s[::-1]

print(palindrome("NIGGIN"))

def count_vowel(s):
    vowel = "aeiou"
    count = 0

    for i in s:
        if i.lower() in vowel:
            count += 1

    return count

print(count_vowel("hello"))