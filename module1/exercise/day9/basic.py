"""
Day 9 Exercises: Basic Trees, Binary Search Trees, Graphs, and Heaps
"""

import heapq

# ==========================================
# 1. Tree Basics (Bank Hierarchy)
# ==========================================
class TreeNode:
    """
    Represents a node in a general tree (e.g., bank organizational hierarchy).
    """
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add_child(self, child_node: 'TreeNode'):
        """Time Complexity: O(1)"""
        self.children.append(child_node)

    def print_tree(self, level: int = 0):
        """
        Prints the hierarchy recursively with indentation.
        Time Complexity: O(N) where N is the total number of nodes in the tree.
        """
        indent = "  " * level
        prefix = "└── " if level > 0 else ""
        print(f"{indent}{prefix}{self.name}")
        for child in self.children:
            child.print_tree(level + 1)


# ==========================================
# 2. Binary Search Tree (BST)
# ==========================================
class BSTNode:
    """
    Represents a single node in a Binary Search Tree.
    """
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        """
        Inserts a new value into the BST.
        Time Complexity: O(h) average, where h is height. O(log N) balanced, O(N) worst case.
        """
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current: BSTNode, value: int):
        if value < current.value:
            if current.left is None:
                current.left = BSTNode(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = BSTNode(value)
            else:
                self._insert_recursive(current.right, value)

    def search(self, value: int) -> bool:
        """
        Searches for a value in the BST.
        Time Complexity: O(log N) average, O(N) worst case.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current: BSTNode, value: int) -> bool:
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)


# ==========================================
# 3. Graph Basics (Customer Transfers)
# ==========================================
class TransferGraph:
    """
    Represents money transfer connections between customers using an Adjacency List.
    """
    def __init__(self):
        self.adjacency_list = {}

    def add_customer(self, customer: str):
        """Time Complexity: O(1)"""
        if customer not in self.adjacency_list:
            self.adjacency_list[customer] = []

    def add_transfer(self, sender: str, receiver: str):
        """
        Adds a directed transfer connection.
        Time Complexity: O(1)
        """
        self.add_customer(sender)
        self.add_customer(receiver)
        self.adjacency_list[sender].append(receiver)

    def print_graph(self):
        """Time Complexity: O(V + E) where V is customers and E is transfers."""
        for customer, connections in self.adjacency_list.items():
            transfers = ", ".join(connections) if connections else "No outbound transfers"
            print(f"{customer} -> [{transfers}]")


# ==========================================
# 4. Heap Basics (Priority Queue for Transactions)
# ==========================================
def demonstrate_heap():
    """
    Uses Python's built-in heapq module to implement a Priority Queue.
    Note: heapq is a min-heap by default. We use numerical priority ranks 
    (Priority 1 highest) to pop highest priority items first.
    """
    priority_queue = []

    # Format: (Priority Rank, Amount, Description)
    # Priority level 1: Fraud Alert (Most urgent)
    # Priority level 2: Big Loan
    # Priority level 3: Small Deposit
    heapq.heappush(priority_queue, (2, 5000, "Big Loan"))
    heapq.heappush(priority_queue, (3, 200, "Small Deposit"))
    heapq.heappush(priority_queue, (1, 10000, "Fraud Alert"))

    print("--- Heap Priority Queue ---")
    # Pop highest priority item -> O(log N)
    prio_level, amount, desc = heapq.heappop(priority_queue)
    print(f"Popped Highest Priority Item: '{desc}' | Amount: {amount} ETB | Priority Rank: {prio_level}")


if __name__ == "__main__":
    print("=== 1. Bank Hierarchy Tree ===")
    head_office = TreeNode("Head Office")
    bole = TreeNode("Bole Branch")
    piassa = TreeNode("Piassa Branch")

    head_office.add_child(bole)
    head_office.add_child(piassa)

    bole.add_child(TreeNode("Teller"))
    bole.add_child(TreeNode("Loan Officer"))

    head_office.print_tree()
    print("\n" + "=" * 35 + "\n")

    print("=== 2. Binary Search Tree ===")
    bst = BinarySearchTree()
    values_to_insert = [50, 30, 70, 20, 40, 60]
    for val in values_to_insert:
        bst.insert(val)

    for target in [40, 100]:
        found = bst.search(target)
        print(f"Search for customer account '{target}': {'Found' if found else 'Not Found'}")
    print("\n" + "=" * 35 + "\n")

    print("=== 3. Transfer Graph ===")
    graph = TransferGraph()
    customers = ["Almaz", "Dawit", "Tigist", "Hanna"]
    for c in customers:
        graph.add_customer(c)

    graph.add_transfer("Almaz", "Dawit")
    graph.add_transfer("Dawit", "Tigist")
    graph.add_transfer("Tigist", "Hanna")
    graph.add_transfer("Almaz", "Hanna")

    graph.print_graph()
    print("\n" + "=" * 35 + "\n")

    demonstrate_heap()