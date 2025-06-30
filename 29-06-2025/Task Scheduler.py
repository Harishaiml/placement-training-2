from collections import Counter

def leastInterval(tasks, n):
    counts = list(Counter(tasks).values())
    max_freq = max(counts)
    max_count = counts.count(max_freq)
    
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
