def combinationSum(candidates, target):
    result = []

    def backtrack(remain, path, start):
        if remain < 0:
            return
        if remain == 0:
            result.append(list(path))
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(remain - candidates[i], path, i)
            path.pop()

    backtrack(target, [], 0)
    return result

# Example usage
print(combinationSum([2, 3, 6, 7], 7))
