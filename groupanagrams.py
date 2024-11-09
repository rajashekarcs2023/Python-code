def groupAnagrams(strs):
    anagram_map = {}
    
    for word in strs:
        # Sort the characters of the word to create a key
        # This ensures all anagrams have the same key
        sorted_word = ''.join(sorted(word))
        
        # Add the word to its anagram group in the map
        # If key doesn't exist, create new list with defaultdict behavior
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(word)
        else:
            anagram_map[sorted_word] = [word]
    
    # Return all the grouped anagrams
    return list(anagram_map.values())

# Test cases
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

print(groupAnagrams([""]))
# Output: [[""]]

print(groupAnagrams(["a"]))
# Output: [["a"]]