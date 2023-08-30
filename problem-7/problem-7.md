### Aproach ###
Implements a router using a trie data structure. Trie structure to manage and retrieve route handlers based on path segments
1. Create RouteTrieNode: This class represents a node in the trie structure.Has 2 attributes is "children" is dictionary of child nodes, "handler" is handler 
2. Create RouteTrie: This class represents the trie structure itself. 
    + Create "insert" method : create nodes and update the handler attribute of the final node. 
    + Create "find" method traverses the trie based on the path segments 
3. Router: This class uses the RouteTrie class to implement the routing functionality.
    + Create split_path: This is a utility method within the Router class that takes a path and splits it into segments

### Run time complexity ###
Insertion (Adding a Route): O(n) time complexity
Lookup (Finding a Route Handler): O(n) time complexity

