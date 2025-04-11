# Write your countBits function here.
def count_bits(n):
    return len(str(bin(n))[2:].replace("0", ""))


print(count_bits(10))
