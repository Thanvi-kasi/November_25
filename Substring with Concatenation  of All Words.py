from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []

        # Try each possible offset within one word length
        for i in range(word_len):
            left = i
            seen = Counter()
            count = 0  # number of words matched

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_count:
                    seen[word] += 1
                    count += 1

                    # If this word appears too many times, shrink from the left
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # If we matched all words exactly once
                    if count == num_words:
                        result.append(left)
                else:
                    # Reset if we encounter a non-matching word
                    seen.clear()
                    count = 0
                    left = j + word_len

        return result
