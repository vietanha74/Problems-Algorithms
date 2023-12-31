class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_parts, handler):
        node = self.root
        for part in path_parts:
            if part not in node.children:
                node.children[part] = RouteTrieNode()
            node = node.children[part]
        node.handler = handler

    def find(self, path_parts):
        node = self.root
        for part in path_parts:
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node.handler

class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        path_parts = self.split_path(path)
        handler = self.route_trie.find(path_parts)
        return handler if handler is not None else self.not_found_handler

    def split_path(self, path):
        parts = []
        for part in path.split("/"):
            if part != "":
                parts.append(part)
        return parts

# Test Cases
root_handler = "Root handler"
not_found_handler = "Not found handler"
router = Router(root_handler, not_found_handler)

# Test Case 1: Empty path should return the root handler
print(router.lookup(""))  # Expected: Root handler

# Test Case 2: Handling a non-existent route with a custom not_found_handler
router.add_handler("about", "About handler")
router.add_handler("blog/2019-01-15/my-awesome-blog-post", "Blog post handler")
print(router.lookup("nonexistent"))  # Expected: Not found handler

# Test Case 3: Handling a route with multiple consecutive slashes (//)
router.add_handler("contact", "Contact handler")
print(router.lookup("contact//info"))  # Expected: Contact handler

# Test Case 4: Handling a route with trailing slashes (/about/)
router.add_handler("about/", "About with trailing slash handler")
print(router.lookup("about/"))  # Expected: About with trailing slash handler
