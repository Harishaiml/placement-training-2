from collections import defaultdict

def accountsMerge(accounts):
    parent = {}

    def find(x):
        if parent.setdefault(x, x) != x:
            parent[x] = find(parent[x])
        return parent[x]

    for account in accounts:
        for email in account[1:]:
            parent[find(email)] = find(account[1])

    unions = defaultdict(list)
    for email in parent:
        unions[find(email)].append(email)

    return [[name] + sorted(emails) for name, emails in 
            [(account[0], unions[find(account[1])]) for account in accounts if find(account[1]) in unions]]
