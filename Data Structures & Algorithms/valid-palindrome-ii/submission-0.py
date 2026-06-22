class Solution:
    def validPalindrome(self, s: str) -> bool:
        first, last = 0, len(s) - 1
        while first < last:

            if s[first] != s[last]:
                # skipping first
                if self.isPalindrome(s[first + 1 : last + 1]):
                    return True
                elif self.isPalindrome(s[first:last]):
                    return True
                else:
                    return False

            first += 1
            last -= 1

        return True

    def isPalindrome(self, s: str) -> bool:

        first, last = 0, len(s) - 1

        while first < last:
            if s[first] != s[last]:
                return False
            first += 1
            last -= 1

        return True
