from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        KEY INSIGHT: 
        Instead of sorting (which costs O(K log K)), we can identify anagrams 
        by their character counts (which costs O(K)). This count acts as a 
        unique 'fingerprint' or 'address' for the group.
        """

        #creating a hash_dict (to use signature as key)
        hash_dict = defaultdict(list)

        for s in strs:
            # 1. Signature Generation: Create a size-26 integer list (for a-z).
            sign_list = [0] * 26 

            for c in s:
                # 2. Mapping: Iterate through the string. For each char, increment the 
                #    index calculated by: ord(char) - ord('a').
                sign_list[ord(c) - ord('a')] += 1

            # 3. Hashing: Convert the list to a TUPLE. Lists are mutable and cannot 
            #    be dictionary keys; tuples are immutable and valid keys.
            hash_dict[tuple(sign_list)].append(s)
        
        #converting to a list
        return list(hash_dict.values())
