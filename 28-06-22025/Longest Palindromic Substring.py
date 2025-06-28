def longestPalindrome(s):
    if len(s) < 2:
        return s

    start, max_len = 0, 1

    for i in range(len(s)):
        low, high = i, i
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

        low, high = i, i + 1
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

    return s[start:start + max_len]
