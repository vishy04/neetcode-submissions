class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        We will format the list to string such that,
        string = [size, separated by comma] +
        $[for marking the start of string] +
        string joined 
        5,5,$HelloWorld
        """
        #for empty strs
        if not strs: return ""

        sizes, res = [], ""

        for s in strs:
            sizes.append(len(s))
        #adding the size separated by comma
        for size in sizes:
            res += str(size)
            res += ","
        #adding * for separation
        res += '*'
        #adding the string in list to res
        for s in strs:
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:

        if not s : return []
        #get back the size list
        sizes , res , i = [], [], 0
        while s[i] != '*':
            cur = ""
            while s[i] !=",":
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        #if not this will start from *
        i += 1
        for sz in sizes:
            res.append(s[i: i + sz])
            i += sz #move by sz to start of next string
        
        return res


