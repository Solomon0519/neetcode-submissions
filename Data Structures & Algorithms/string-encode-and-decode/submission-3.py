import re

class Solution:

    def encode(self, strs: List[str]) -> str:

        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        
        matches = []
        pos = 0

        while pos < len(s):

            curr = pos

            while s[curr] != '#':
                curr += 1

            string_length = int(s[pos : curr])
            match = s[curr + 1 : curr + 1 + string_length]

            matches.append(match)

            pos = curr + 1 + string_length

        return matches
        