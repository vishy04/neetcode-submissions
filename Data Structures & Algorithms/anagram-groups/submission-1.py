from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        instead of using the sorted str as a key for hash , 
        we can use freq_hash of size 26 as a key, 
        freq_hash is nothing but count of each letter[like address] ,
        address of all anagram is same
        """
        #creating a hash_dict (to use signature as key)
        hash_dict = defaultdict(list)

        for s in strs:
            sign_list = [0] * 26 

            for c in s:
                sign_list[ord(c) - ord('a')] += 1

            #key has to be a tuple in dict
            hash_dict[tuple(sign_list)].append(s)
        
        return list(hash_dict.values())
