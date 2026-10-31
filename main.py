from models.binary_tree import BinaryTree

tree = BinaryTree()

tree.insert("Documents", True)
tree.insert("Backups", True)
tree.insert("Pictures", True)
tree.insert("Archive", True)
tree.insert("Photos", True)

print("Before:", tree.in_order())

result = tree.delete("Documents")

print("Deleted:", result)
print("After:", tree.in_order())