"""
Mini Project: Bank Customer Service Simulator (Addis Bank)
"""

class AddisBankSimulator:
    def __init__(self):
        # Stack for transaction history (LIFO) -> O(1) append/pop
        self.transaction_history = []
        
        # Dictionary for fast customer lookup by account number -> O(1) lookup
        self.customers = {
            "1001": {"name": "Abebe Bikila", "balance": 15000.0},
            "1002": {"name": "Almaz Ayana", "balance": 24500.0},
            "1003": {"name": "Haile Gebrselassie", "balance": 50000.0}
        }

    def make_transaction(self, acc_num: str, amount: float):
        """
        Executes a transaction and pushes to history stack.
        Time Complexity: O(1)
        """
        if acc_num not in self.customers:
            print("Error: Account number not found!")
            return

        self.customers[acc_num]["balance"] += amount
        transaction_record = {
            "acc_num": acc_num,
            "amount": amount
        }
        
        # Push to stack
        self.transaction_history.append(transaction_record)
        print(f"Success: Processed {'Deposit' if amount > 0 else 'Withdrawal'} of {abs(amount)} ETB for Account {acc_num}.")

    def undo_last_transaction(self):
        """
        Pops the last transaction from stack and reverts balance.
        Time Complexity: O(1)
        """
        if not self.transaction_history:
            print("No transactions to undo.")
            return

        # Pop from stack
        last_tx = self.transaction_history.pop()
        acc_num = last_tx["acc_num"]
        amount = last_tx["amount"]

        # Revert balance
        self.customers[acc_num]["balance"] -= amount
        print(f"Undo Successful: Reverted {amount} ETB on Account {acc_num}.")

    def search_customer(self, acc_num: str):
        """
        Searches customer using dictionary lookup.
        Time Complexity: O(1)
        """
        customer = self.customers.get(acc_num)
        if customer:
            print(f"\n--- Customer Info ---")
            print(f"Account: {acc_num}")
            print(f"Name:    {customer['name']}")
            print(f"Balance: {customer['balance']} ETB\n")
        else:
            print("Customer not found.")

    def run(self):
        while True:
            print("\n=== Addis Bank Customer Service ===")
            print("1. Make a transaction")
            print("2. Undo last transaction")
            print("3. Search customer by account number")
            print("4. Exit")
            
            choice = input("Enter choice (1-4): ").strip()

            if choice == "1":
                acc = input("Enter account number (e.g., 1001): ").strip()
                try:
                    amt = float(input("Enter amount (positive for deposit, negative for withdrawal): "))
                    self.make_transaction(acc, amt)
                except ValueError:
                    print("Invalid amount format!")

            elif choice == "2":
                self.undo_last_transaction()

            elif choice == "3":
                acc = input("Enter account number: ").strip()
                self.search_customer(acc)

            elif choice == "4":
                print("Thank you for using Addis Bank Services!")
                break
            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    simulator = AddisBankSimulator()
    simulator.run()