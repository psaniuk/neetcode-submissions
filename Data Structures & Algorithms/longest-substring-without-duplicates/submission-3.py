class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        uniqueSubset = set()
        left, right = 0, 0

        while right < len(s):    
            while s[right] in uniqueSubset:
                uniqueSubset.remove(s[left])
                left += 1

            uniqueSubset.add(s[right])
            result = max(result, len(uniqueSubset))

            right += 1

            
        return result






















