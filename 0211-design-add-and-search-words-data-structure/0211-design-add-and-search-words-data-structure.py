class TrieNode: #Time O(M) Space (M*N) m average len of words n num of words
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_word      
            if word[index] == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
            else:
                if word[index] in node.children:
                    return dfs(node.children[word[index]], index + 1)  
            return False
        return dfs(self.root, 0)