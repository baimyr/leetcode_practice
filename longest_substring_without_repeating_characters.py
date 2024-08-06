class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final_len = 0
        current_len = 0
        letters = deque()
        pointer = 0
        s_len = len(s)
        final_letter = s_len - 1
        while pointer < s_len:
            letter = s[pointer]
            is_final = pointer 
            if letter in letters:
                if current_len > final_len:
                    final_len = current_len
                pointer = pointer - current_len + letters.index(letter) + 1
                letters.clear()
                current_len = 0
                continue
            current_len += 1
            if pointer == final_letter:
                if current_len > final_len:
                    final_len = current_len
            pointer += 1
            letters.append(letter)
        return final_len