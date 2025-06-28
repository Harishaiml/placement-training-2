def permute(nums):
    result = []

    def backtrack(path, options):
        if not options:
            result.append(path)
            return
        for i in range(len(options)):
            # Recurse with the current element added to path and the rest as options
            backtrack(path + [options[i]], options[:i] + options[i+1:])

    backtrack([], nums)
    return result

# Example usage
print(permute([1, 2, 3]))
