def partitionLabels(s):
    last = {c: i for i, c in enumerate(s)}
    res = []
    j = anchor = 0
    for i, c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            res.append(i - anchor + 1)
            anchor = i + 1
    return res
