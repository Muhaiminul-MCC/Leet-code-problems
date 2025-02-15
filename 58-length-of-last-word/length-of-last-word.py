class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.split()[-1]
        last_word_length = len(last_word)
        return last_word_length

