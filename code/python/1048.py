class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda s: len(s))
        str_to_chainlen = collections.Counter()
        max_length = 0
        for i, w in enumerate(words):
            for j in range(len(w)):
                curr_w = w[:j] + w[j+1:]
                str_to_chainlen[w] = max(str_to_chainlen[w], str_to_chainlen[curr_w] + 1)
            max_length = max(max_length, str_to_chainlen[w])
        return max_length
