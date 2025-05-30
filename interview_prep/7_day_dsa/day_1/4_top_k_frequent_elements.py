"""
# 4. Top K Frequent Elements
Problem: Return k most frequent elements in array.
Input: [1,1,1,2,2,3], k = 2 → Output: [1,2]
Constraints: Use heap or bucket sort to beat O(n log n)
"""

def top_k_frequency_elements(nums, k):
    print(nums, k)
    freq_map = {}

    for num in nums:
        if num not in freq_map:
            freq_map[num] = 0
        freq_map[num] += 1

    n = len(nums)

    buckets = [[] for _ in range(n+1)]
    for num, freq in freq_map.items():
        buckets[freq].append(num)

    result = []

    for i in range(n, 0, -1):
        for num in buckets[i]:
            result.append(num)

            if len(result) == k:
                break

    return result

print(top_k_frequency_elements(nums=[1,1,1,2,2,3], k = 2))