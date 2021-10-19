class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = sorted(words, key=lambda x: len(x))
        min_len = max(1, len(words[0]))
        mem = set()
        res = []

        def checkMem(word):
            if word in mem: return True
            for i in range(min_len, len(word) - min_len + 1):
                if word[:i] in mem and checkMem(word[i:]):
                    return True
            return False

        for word in words:
            if checkMem(word) == True:
                res.append(word)
            mem.add(word)
        return res