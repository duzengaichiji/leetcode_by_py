class WordDictionary:

    def __init__(self):
        self.lookup = {}


    def addWord(self, word: str) -> None:
        tree = self.lookup
        for char in word:
            if char not in tree:
                tree[char] = {}
            tree = tree[char]
        tree['#'] = word

    def search(self, word: str) -> bool:
        def searchDF(tree,word):
            if not isinstance(tree,dict): return False
            if len(word)==0:
                return '#' in tree
            if word[0]=='.':
                for key,value in tree.items():
                    if searchDF(value,word[1:]): return True
                return False
            else:
                if word[0] in tree:
                    return searchDF(tree[word[0]],word[1:])
                return False
        tree = self.lookup
        return searchDF(tree,word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)