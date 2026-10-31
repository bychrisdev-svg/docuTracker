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