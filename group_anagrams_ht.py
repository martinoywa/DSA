# Link: https://leetcode.com/problems/group-anagrams/
# Time Complexity: O(N * k log k)
# Space Complexity: O(N * k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs: # O(N)
            _  = "".join(sorted(s)) # O(k log k)
            if groups.get(_) is not None:
                groups[_].append(s)
            else:
                groups[_] = [s]

        return list(groups.values())
    
