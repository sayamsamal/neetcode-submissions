class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for w in strs:
            sw = "".join(sorted(w))
            if sw in anagrams:
                anagrams[sw].append(w)
            else:
                anagrams[sw] = [w]
        return list(anagrams.values())