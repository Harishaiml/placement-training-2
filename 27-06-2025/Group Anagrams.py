from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)

    # Iterate through each word in the input list
    for word in strs:
        # Sort the word to use as a key (e.g., "bat" becomes "abt")
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)  # Group the original word

    # Return grouped anagrams as a list
    return list(anagrams.values())

# Example usage
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input_list))
