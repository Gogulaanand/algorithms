
https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= {}
        print(sorted(strs))
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
            
            