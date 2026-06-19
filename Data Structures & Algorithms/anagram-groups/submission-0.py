class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        KEY INSIGHT: Anagrams share the same 'canonical form' when sorted.
        (e.g., "eat", "tea", "ate" all become "aet" when characters are sorted).
        """
        
        # Algorithm:
        # 1.Map Initialization: Use a hash map (dictionary) to group strings.

        hash_dict = defaultdict(list)

        # 2. Key Generation: For every string in the input list, sort it to generate a unique key.
        for s in strs:

            #sorted(s)-> For eat give ['a','e','t'] ->so we join them
            s_sorted = ''.join(sorted(s))

            # 3. Grouping: Append the original string to the list corresponding to its sorted key.
            hash_dict[s_sorted].append(s)

        # 4. Output: Return all values from the dictionary (the grouped lists).
        return list(hash_dict.values())
        
        
        