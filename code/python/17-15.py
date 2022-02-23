class Solution:
    def longestWord(self, words: List[str]) -> str:
        # dfs寻找，可以拆成组内其他词的单词
        words = sorted(words, key = lambda x:len(x))
        res = ""
        trie = {}

        def search(word, root, node):
            if not word:
                return True
            for i in range(len(word)):
                if word[i] not in node:
                    return False
                if '#' in node[word[i]]:
                    if search(word[i+1:],root,root):
                        return True
                node = node[word[i]]
            return False


        for word in words:
            root = trie
            if search(word, trie, trie):
                if len(word)>len(res):
                    res = word
                elif len(word)==len(res):
                    res = word if res>word else res
            for char in word:
                if char not in root:
                    root[char] = {}
                root = root[char]
            root['#'] = word
        return res