class Solution(object):
    def wonderfulSubstrings(self, word):
        count = [0] * 1024
        count[0] = 1  # Empty string is wonderful

        bitmask = 0
        result = 0

        for c in word:
            bitmask ^= 1 << (ord(c) - ord('a'))
            result += count[bitmask]
            
            for i in range(10):
                result += count[bitmask ^ (1 << i)]
            
            count[bitmask] += 1

        return result