class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        matches = deque()
        for index, symbol in enumerate(haystack):
            if symbol == needle[0]:
                matches.append('')
            match_index = 0
            while match_index < len(matches):
                match = matches[match_index]
                possible_match = match + symbol
                if needle.startswith(possible_match):
                    match = possible_match
                    matches[match_index] = possible_match
                else:
                    del matches[match_index]
                    continue
                match_len = len(match)
                if match_len == needle_len:
                    return index - match_len + 1

                match_index += 1
            
        return -1
