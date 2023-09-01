### Aproach ###
To solve this problem, we can follow these steps:
1. Create The RouteTrieNode class represents a node in a routing trie
    - The children attribute is a dictionary that maps strings to RouteTrieNode
    - The handler attribute is the path represented by the node is matched.

2. Create RouteTrie class represents a routing trie
    - The root attribute is a RouteTrieNode object that represents the root of the trie.
    - The insert() function inserts a new path and handler into the trie. 
    - The find() method of the RouteTrie class finds the handler for a given path.
   
3. The Router class is a wrapper class for the RouteTrie class.
    - The split_path() function splits a path into a list of path parts.
    - The lookup() function looks up the handler for a given path. 
        + If the path is found => returns the handler. 
        + Else => returns the not_found_handler value.

### Run time complexity ###
Insertion (Adding a Route): O(n) time complexity
Lookup (Finding a Route Handler): O(n) time complexity
Overall, the runtime complexity of the RouteTrie class and the Router class is O(n), where n is the length of the longest path.


### Space complexity ###
1.The RouteTrie class has a space complexity of O(n) because it needs to store a node for each path that is inserted into the trie.
2.The Router class has a space complexity of O(n + m) because it needs to store a RouteTrie object for each path that is added to the router and it needs to store the handlers that are associated with the paths.


