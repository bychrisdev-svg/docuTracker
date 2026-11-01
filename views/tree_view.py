class TreeView:

    @staticmethod
    def display_tree(root):

        if root is None:
            print("Tree is empty.")
            return

        print(root.name)

        TreeView._display_children(root, "")

    @staticmethod
    def _display_children(node, prefix):

        children = []

        if node.left is not None:
            children.append(node.left)

        if node.right is not None:
            children.append(node.right)

        for index, child in enumerate(children):

            is_last = index == len(children) - 1

            connector = "└── " if is_last else "├── "

            print(prefix + connector + child.name)

            extension = "    " if is_last else "│   "

            TreeView._display_children(
                child,
                prefix + extension
            )

    @staticmethod
    def display_traversals(tree):

        print("\n========== TREE TRAVERSALS ==========")

        print("In-order:", " -> ".join(tree.in_order()))

        print("Pre-order:", " -> ".join(tree.pre_order()))

        print("Post-order:", " -> ".join(tree.post_order()))

        print("Level-order:", " -> ".join(tree.level_order()))

        print("=====================================")

    @staticmethod
    def display_height(tree):

        print(f"\nTree height: {tree.height()}")