## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_end_of_word = False
    
    def insert(self,char):
        if char not in self.children:
            self.children[char] = TrieNode()  

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        results = []

        if self.is_end_of_word and suffix != '':
            results.append(suffix)
        
        for char,child_node in self.children.items():
            results.extend(child_node.suffixes(suffix+char))
        
        return results

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
    
    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True
    
    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Interactive function to find words with a given prefix
def find(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print("Words with prefix '{}':".format(prefix))
            print('\n'.join(prefixNode.suffixes()))
        else:
            print("No words found with prefix '{}'".format(prefix))
    else:
        print('Please enter a prefix.')

# Test cases

# Edge Case 1: Empty Trie
emptyTrie = Trie()
find("empty")  # Should print "Please enter a prefix."

# Edge Case 2: Prefix not found
find("xyz")  # Should print "No words found with prefix 'xyz'"
