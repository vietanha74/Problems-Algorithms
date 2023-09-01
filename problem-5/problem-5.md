### Aproach ###
To solve this problem, we can follow these steps:
1. Create TrieNode class represents a single node in the trie:
    -  two attributes: children and is_end_of_word
        +  Children is a dictionary that maps characters to child nodes
        +  is_end_of_word attribute is a boolean flag indicates node represents the end of a word.
    - suffixes function :
        +  Initializes a list called results
        +  Checks if the node represents the end of a word =>  appends the suffix to the list of results
        +  Iterates over the children of the node. For each child node recursively calls the suffixes() function => appends the child node's suffixes to the list of results.
    
2. The Trie class represents the trie itself. 
    - One attribute: root it is a reference to the root node of the trie.
    - Insert function :  takes a word as input and inserts it into the trie
        + First setting the current node to the root node
        + Iterates over the characters in the word.
        + For each character, the function checks 
            a. if the character is already present in the children of the current node.
            b. If the character is not present,  creates a new node for the character and adds it to the children of the current node.
            c. Sets the current node to the newly created node.
        +  Sets the is_end_of_word of the current node to True indicates that the current node represents the end of a word.
    - Find function :
        + First setting the current node to the root node
        + Iterates over the characters in the prefix. For each character, the function checks
            a. If the character is not present, the function returns None
            b. Else sets the current node to the child node 

### Run time complexity ###
The run time complexity of the trie data structure depends on the number of words that are inserted into the trie. Where m is the number of words in the trie and n is the average length of the words.
=> The average case run time complexity is O(m*n)
### Space complexity ###
The space complexity of a trie is O(m*n), where m is the number of characters in the alphabet and n is the average length of the words in the trie.

