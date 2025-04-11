# Write your totalPrime function here.
def total_prime(s, e):
    res = []
    for i in range(s, e + 1):
        for j in range(1, i):
            if i % j != 0 and i != 1 and i != j:
                res.append(j)

    return list(sorted(set(res)))


print(total_prime(2, 10))
