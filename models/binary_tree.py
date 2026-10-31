from models.node import Node
from collections import deque

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, name, is_folder):

        new_node = Node(name, is_folder)

        if self.root is None:
            self.root = new_node
            return True

        current = self.root

        while True:
            if not current.is_folder:
                return False
            if name.casefold() < current.name.casefold():
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            elif name.casefold() > current.name.casefold():
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right
            else:
                return False

    def search(self, name):

        current = self.root
        comparisons = 0

        while current is not None:

            comparisons += 1

            if name.casefold() == current.name.casefold():
                return current, comparisons

            elif name.casefold() < current.name.casefold():
                current = current.left

            else:
                current = current.right

        return None, comparisons

    def _find_node(self, name):

        current = self.root
        parent = None

        while current is not None:

            if name.casefold() == current.name.casefold():
                return current, parent

            parent = current

            if name.casefold() < current.name.casefold():
                current = current.left
            else:
                current = current.right

        return None, None

    def delete(self, name):

        node, parent = self._find_node(name)

        if node is None:
            return False

        if node.left is None and node.right is None:

            if parent is None:
                self.root = None

            elif parent.left == node:
                parent.left = None

            else:
                parent.right = None

            return True

        if node.left is None or node.right is None:

            child = node.left if node.left is not None else node.right

            if parent is None:
                self.root = child

            elif parent.left == node:
                parent.left = child

            else:
                parent.right = child

            return True

        if node.left is not None and node.right is not None:

            successor_parent = node
            successor = node.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            node.name = successor.name
            node.is_folder = successor.is_folder

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

            return True

        return False

    def in_order(self):

        result = []

        def traverse(current):

            if current is not None:

                traverse(current.left)
                result.append(current.name)
                traverse(current.right)

        traverse(self.root)

        return result

    def pre_order(self):
    
            result = []
    
            def traverse(current):
    
                if current is not None:
    
                    result.append(current.name)
                    traverse(current.left)
                    traverse(current.right)
    
            traverse(self.root)
    
            return result

    def post_order(self):
        
                result = []
        
                def traverse(current):
        
                    if current is not None:
        
                        traverse(current.left)
                        traverse(current.right)
                        result.append(current.name)
        
                traverse(self.root)
        
                return result

    def level_order(self):
        result = []
        queue = deque()

        if self.root is not None:
            queue.append(self.root)

        while queue:
            current = queue.popleft()
            result.append(current.name)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return result

    def height(self):

        def calculate_height(current):
            
            if current is None:
                return 0

            left_height = calculate_height(current.left)
            right_height = calculate_height(current.right)

            return 1 + max(left_height, right_height)

        return calculate_height(self.root)