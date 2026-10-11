class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        current = self.tree
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        
        current['.'] = True
    def search(self, word: str) -> bool:
        current = self.tree
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return '.' in current

    def startsWith(self, prefix: str) -> bool:
        current = self.tree
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True