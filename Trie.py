class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.next = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(0)


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.root = self._insert(self.root, word, 0)

    def _insert(self, root, word, start):
        if start == len(word):
            root.val = True
            return root

        if not root:
            root = TrieNode()
        if word[start] in root.next:
            # the most import thing is root.next[word[start]] = self._insert(root.next[word[start]], word, start+1) instead of root = self._insert(root.next[word[start]], word, start+1)
            root.next[word[start]] = self._insert(root.next[word[start]], word, start+1)
        else:
            root.next[word[start]] = self._insert(None, word, start+1)
        return root



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self._search(self.root, word, 0)

    def _search(self, root, word, start):
        if start == len(word):
            return root.val
        if word[start] in root.next:
            return self._search(root.next[word[start]], word, start+1)
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self._startWith(self.root, prefix, 0)

    def _startWith(self, root, word, start):
        if start == len(word):
            return True
        if word[start] in root.next:
            return self._search(root.next[word[start]], word, start+1)
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)