# ==========================================
# File: utils.py
# Purpose: Module containing utility functions
# ==========================================

def add_tax(price, rate=0.15):
    """
    Calculates and returns the final price after adding tax.
    
    Parameters:
        price (float): The base price of the item.
        rate (float): Tax rate as a decimal (default is 0.15 or 15%).
        
    Returns:
        float: Total price including tax.
    """
    # Print the internal process step
    print(f"  [utils.py] Processing price: ${price:.2f} with tax rate: {rate * 100:.1f}%")
    
    # Calculate tax amount
    tax_amount = price * rate
    print(f"  [utils.py] Calculated tax amount: ${tax_amount:.2f}")
    
    # Calculate total price including tax
    total_price = price + tax_amount
    
    return total_price
# At the end of the file:
result = add_tax(100)
print(f"Final price: ${result:.2f}")