def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest
