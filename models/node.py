class Node:
    def __init__(self, name, is_folder):
        self.name = name
        self.is_folder = is_folder
        self.right = None
        self.left = None