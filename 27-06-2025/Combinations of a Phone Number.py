def letterCombinations(digits):
    if not digits:
        return []

    phone = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    res = []

    def backtrack(index, path):
        if index == len(digits):
            res.append(path)
            return

        possible_letters = phone[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)

    backtrack(0, "")
    return res

# Example usage
print(letterCombinations("23"))
