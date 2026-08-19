"""
Mini Project: Addis Bank Network & Priority System
Combines Trees, Binary Search Trees, Graphs, and Heaps into a console application.
"""

import heapq
from collections import deque


# ==========================================
# 1. Tree: Branch Hierarchy
# ==========================================
class TreeNode:
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add_child(self, child_node: 'TreeNode'):
        """Time Complexity: O(1)"""
        self.children.append(child_node)

    def print_tree(self, level: int = 0):
        """Time Complexity: O(N) where N is total tree nodes."""
        indent = "  " * level
        prefix = "└── " if level > 0 else ""
        print(f"{indent}{prefix}{self.name}")
        for child in self.children:
            child.print_tree(level + 1)


# ==========================================
# 2. BST: Customer Account Search
# ==========================================
class AccountNode:
    def __init__(self, account_num: int, name: str):
        self.account_num = account_num
        self.name = name
        self.left = None
        self.right = None


class AccountBST:
    def __init__(self):
        self.root = None

    def insert(self, account_num: int, name: str):
        """Time Complexity: O(log N) average, O(N) worst case."""
        if not self.root:
            self.root = AccountNode(account_num, name)
        else:
            self._insert_recursive(self.root, account_num, name)

    def _insert_recursive(self, current: AccountNode, account_num: int, name: str):
        if account_num < current.account_num:
            if current.left is None:
                current.left = AccountNode(account_num, name)
            else:
                self._insert_recursive(current.left, account_num, name)
        elif account_num > current.account_num:
            if current.right is None:
                current.right = AccountNode(account_num, name)
            else:
                self._insert_recursive(current.right, account_num, name)

    def search(self, account_num: int) -> AccountNode:
        """Time Complexity: O(log N) average, O(N) worst case."""
        return self._search_recursive(self.root, account_num)

    def _search_recursive(self, current: AccountNode, account_num: int) -> AccountNode:
        if current is None or current.account_num == account_num:
            return current
        if account_num < current.account_num:
            return self._search_recursive(current.left, account_num)
        return self._search_recursive(current.right, account_num)


# ==========================================
# 3. Graph: Transfer Network (BFS & DFS)
# ==========================================
class CustomerNetworkGraph:
    def __init__(self):
        self.adj_list = {}

    def add_customer(self, customer: str):
        """Time Complexity: O(1)"""
        if customer not in self.adj_list:
            self.adj_list[customer] = []

    def add_transfer(self, sender: str, receiver: str):
        """Time Complexity: O(1)"""
        self.add_customer(sender)
        self.add_customer(receiver)
        self.adj_list[sender].append(receiver)

    def bfs(self, start_customer: str):
        """
        Breadth-First Search (BFS) to traverse connections level-by-level.
        Time Complexity: O(V + E) where V = customers, E = transfers.
        Space Complexity: O(V)
        """
        if start_customer not in self.adj_list:
            print(f"Customer '{start_customer}' not found in network.")
            return

        visited = set([start_customer])
        queue = deque([start_customer])
        traversal = []

        while queue:
            curr = queue.popleft()
            traversal.append(curr)
            for neighbor in self.adj_list[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print(f"BFS Connection Network starting from {start_customer}: " + " -> ".join(traversal))

    def dfs(self, start_customer: str):
        """
        Depth-First Search (DFS) to traverse deeply along transfer paths.
        Time Complexity: O(V + E) where V = customers, E = transfers.
        Space Complexity: O(V)
        """
        if start_customer not in self.adj_list:
            print(f"Customer '{start_customer}' not found in network.")
            return

        visited = set()
        traversal = []

        def _dfs_recursive(customer: str):
            visited.add(customer)
            traversal.append(customer)
            for neighbor in self.adj_list[customer]:
                if neighbor not in visited:
                    _dfs_recursive(neighbor)

        _dfs_recursive(start_customer)
        print(f"DFS Connection Network starting from {start_customer}: " + " -> ".join(traversal))


# ==========================================
# 4. Heap: Urgent Transaction System
# ==========================================
class PriorityTransactionSystem:
    def __init__(self):
        self.heap = []
        self.counter = 0  # Sequence counter for FIFO tie-breaking on identical priorities

    def add_transaction(self, priority: int, description: str, amount: float):
        """
        Pushes urgent transaction to Min-Heap based on priority rank (1 = Highest).
        Time Complexity: O(log N)
        """
        heapq.heappush(self.heap, (priority, self.counter, description, amount))
        self.counter += 1
        print(f"Added Transaction: '{description}' with Priority Level {priority}.")

    def process_highest_priority(self):
        """
        Pops and processes the highest priority transaction.
        Time Complexity: O(log N)
        """
        if not self.heap:
            print("No pending priority transactions.")
            return

        priority, _, description, amount = heapq.heappop(self.heap)
        print(f"\nProcessing Priority Level {priority} Transaction:")
        print(f"  Description: {description}")
        print(f"  Amount:      {amount:.2f} ETB\n")


# ==========================================
# Main Application Logic
# ==========================================
class AddisBankSystem:
    def __init__(self):
        # Tree Setup
        self.root_office = TreeNode("Addis Bank Head Office")
        
        # BST Setup
        self.account_bst = AccountBST()
        self.account_bst.insert(1005, "Abebe Bikila")
        self.account_bst.insert(1002, "Almaz Ayana")
        self.account_bst.insert(1008, "Haile Gebrselassie")

        # Graph Setup
        self.transfer_network = CustomerNetworkGraph()

        # Heap Setup
        self.priority_system = PriorityTransactionSystem()

    def run(self):
        while True:
            print("\n=== Addis Bank Network & Priority System ===")
            print("1. Add new branch / employee (Tree)")
            print("2. Display Bank Hierarchy (Tree)")
            print("3. Add money transfer connection (Graph)")
            print("4. Show connected customers using BFS/DFS (Graph)")
            print("5. Add urgent transaction (Heap)")
            print("6. Process highest priority transaction (Heap)")
            print("7. Search for customer account in BST (BST)")
            print("8. Exit")

            choice = input("Select choice (1-8): ").strip()

            if choice == "1":
                node_name = input("Enter new branch or employee name: ").strip()
                new_node = TreeNode(node_name)
                self.root_office.add_child(new_node)
                print(f"Added '{node_name}' under '{self.root_office.name}'.")

            elif choice == "2":
                print("\n--- Addis Bank Hierarchy ---")
                self.root_office.print_tree()

            elif choice == "3":
                sender = input("Enter sender customer name: ").strip()
                receiver = input("Enter receiver customer name: ").strip()
                self.transfer_network.add_transfer(sender, receiver)
                print(f"Recorded transfer connection: {sender} -> {receiver}")

            elif choice == "4":
                start_name = input("Enter starting customer name: ").strip()
                print("\n--- BFS Traversal ---")
                self.transfer_network.bfs(start_name)
                print("--- DFS Traversal ---")
                self.transfer_network.dfs(start_name)

            elif choice == "5":
                desc = input("Enter transaction description (e.g., Fraud Alert): ").strip()
                try:
                    amt = float(input("Enter amount: "))
                    prio = int(input("Enter priority level (1 = Highest, 2 = Medium, 3 = Low): "))
                    self.priority_system.add_transaction(prio, desc, amt)
                except ValueError:
                    print("Invalid numerical input.")

            elif choice == "6":
                self.priority_system.process_highest_priority()

            elif choice == "7":
                try:
                    acc_num = int(input("Enter account number to search: "))
                    node = self.account_bst.search(acc_num)
                    if node:
                        print(f"Account Found! Account #: {node.account_num}, Name: {node.name}")
                    else:
                        print(f"Account number '{acc_num}' not found.")
                except ValueError:
                    print("Please enter a valid integer account number.")

            elif choice == "8":
                print("Exiting System.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    app = AddisBankSystem()
    app.run()