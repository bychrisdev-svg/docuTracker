from models.binary_tree import BinaryTree
from views.tree_view import TreeView


class TreeController:

    def __init__(self):
        self.tree = BinaryTree()
        self.view = TreeView()

    def run(self):
        print("================================")
        print("       DOCUTRACK SYSTEM")
        print("================================")

        self.load_initial_data()

        self.view.display_tree(self.tree.root)
        self.view.display_traversals(self.tree)
        self.view.display_height(self.tree)

    def load_initial_data(self):

        initial_data = [
            
            # Folders
            ("Documents", True),
            ("Backups", True),
            ("Pictures", True),
            ("Downloads", True),
            ("Music", True),
            ("Projects", True),
            ("Reports", True),
            ("Work", True),

            # Files
            ("Archive.zip", False),
            ("Budget.xlsx", False),
            ("Dov.txt", False),
            ("Dzz.txt", False),
            ("Nova.txt", False),
            ("Pq.txt", False)
        ]

        print("\n========== LOADING DATA ==========")

        for name, is_folder in initial_data:

            success, comparisons = self.tree.insert(name, is_folder)

            if success:
                print(
                    f"Inserted: {name} "
                    f"({comparisons} comparisons)"
                )
            else:
                print(f"Could not insert: {name}")

        print(f"\nTotal nodes loaded: {len(initial_data)}")
        print("==================================")