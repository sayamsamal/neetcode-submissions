class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False
        
        map_s1 = defaultdict(int)
        for c in s1:
            map_s1[c] += 1
        
        map_s2 = defaultdict(int)
        l = 0
        r = 0
        while r < s2_len:
            map_s2[s2[r]] += 1

            if map_s2 == map_s1:
                return True

            if r - l + 1 >= s1_len:
                map_s2[s2[l]] -= 1
                if map_s2[s2[l]] == 0:
                    map_s2.pop(s2[l])
                l += 1
            r += 1
        
        print(map_s1)
        return False
