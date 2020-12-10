class Trie:
    def __init__(self):
        self.lookup = {}
    def insert(self,word):
        tree = self.lookup
        for c in word[:-1]:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        res = False
        if "#" in tree:
            res=True
        if word[-1] not in tree:
            tree[word[-1]] = {}
        tree = tree[word[-1]]
        tree['#'] = '#'
        if len(word)==1:
            res = True
        return res
    def search(self,word):
        tree = self.lookup
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        if '#' not in tree:
            return False
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordDict = set(words)
        trie = Trie()
        words = sorted(words,key=lambda x:(len(x),x))
        res = []
        for word in words:
            if trie.insert(word)==True:
                temp = True
                for i in range(1,len(word)):
                    if word[:i] not in wordDict:
                        temp=False
                        break
                if temp==True:
                    if not res or len(word)>len(res[-1]):
                        res = [word]
                    else:
                        res.append(word)
        return sorted(res)[0] if len(res)>0 else ""