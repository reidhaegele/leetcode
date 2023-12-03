from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
                for c in s:
                        if c in hm:
                                hm[c] = hm[c] + 1
                        
                        
