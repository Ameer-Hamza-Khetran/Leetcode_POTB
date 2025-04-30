class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        def is_subsequence(word, s):
            i = 0
            j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            return i == len(word)

        def is_lex_smaller(w1, w2):
            min_len = len(w1) if len(w1) < len(w2) else len(w2)
            for i in range(min_len):
                if w1[i] < w2[i]:
                    return True
                elif w1[i] > w2[i]:
                    return False
            return len(w1) < len(w2)

        def find_longest_word(s, dictionary):
            best_word = ""
            for word in dictionary:
                if is_subsequence(word, s):
                    if len(word) > len(best_word):
                        best_word = word
                    elif len(word) == len(best_word) and is_lex_smaller(word, best_word):
                        best_word = word
            return best_word

        # \U0001f525 THE MISSING PIECE
        return find_longest_word(s, dictionary)
