from models.binary_tree import BinaryTree

tree = BinaryTree()
tree.insert("Documents", True)
tree.insert("Backups", True)
tree.insert("Pictures", True)

print("In-order:", tree.in_order())
print("Pre-order:", tree.pre_order())
print("Post-order:", tree.post_order())
print("Level-order:", tree.level_order())