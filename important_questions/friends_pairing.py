"""
You are given an integer ‘N’, which denotes there are ‘N’ friends.
You are supposed to form some pairs them satisfying the following conditions:
    1. Each friend can be paired with some other friend or remain single.
    2. Each friend can be a part of at most one pair.
You are supposed to find the total number of ways in which the pairing can be done satisfying both conditions.
Since the number of ways can be quite large, you should find the answer modulo 1000000007(10^9+7).

Note:
    1. Return the final answer by doing a mod with 10^9 + 7.
    2. Pairs {A, B} and {B, A} are considered the same

Problem approach
For n-th person there are two choices:
    1. n-th person remains single, we recur for f(n – 1).
    2. n-th person pairs up with any of the remaining n – 1 persons. We get (n – 1) * f(n – 2).
There-fore we can recursively write f(n) as: f(n) = f(n – 1) + (n – 1) * f(n – 2).

We can simply form the recursive function for it with base case if n<=2 then f(n) = n as f(1)=1 and f(2)=2.

"""
