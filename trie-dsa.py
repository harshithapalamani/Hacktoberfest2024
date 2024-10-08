class TrieNode:
    def __init__(self):
        # Each TrieNode contains a dictionary of children and a boolean to mark the end of a word
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # The root of the Trie is an empty TrieNode
        self.root = TrieNode()

    def insert(self, word):
        # Insert a word into the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                # If the character is not present, add it to the current node's children
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        # Mark the end of the word
        current_node.is_end_of_word = True

    def search(self, word):
        # Search for a word in the Trie, returns True if the word exists
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        # Check if there is any word in the Trie that starts with the given prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))  # True
print(trie.search("app"))    # True
print(trie.search("appl"))   # False
print(trie.starts_with("app"))  # True
print(trie.starts_with("bat"))  # False
