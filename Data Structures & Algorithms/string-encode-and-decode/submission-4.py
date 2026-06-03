from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += f"{len(i)}#{i}"
        return ans
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # ✅ Moved outside
            i = j + 1             # Move past '#'
            res.append(s[i:i+length])  # Extract string
            i = i + length        # Move to next encoded chunk
        return res
