def calculate_profit_margin(revenue, cost):
    """Calculate profit margin as a percentage."""
    if revenue <= 0:
        return 0
    profit = revenue - cost
    return (profit / revenue) * 100

def calculate_roi(gain_from_investment, cost_of_investment):
    """Calculate Return on Investment (ROI) as a percentage."""
    if cost_of_investment <= 0:
        return 0
    return ((gain_from_investment - cost_of_investment) / cost_of_investment) * 100

def calculate_break_even_point(fixed_costs, price_per_unit, variable_cost_per_unit):
    """Calculate break-even point in units."""
    contribution_margin = price_per_unit - variable_cost_per_unit
    if contribution_margin <= 0:
        return float('inf')
    return fixed_costs / contribution_margin

class StockManager:
    def __init__(self):
        self.inventory = {}

    def add_stock(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        print(f"Added {quantity} of {item_name}. Total: {self.inventory[item_name]}")

    def remove_stock(self, item_name, quantity):
        if item_name in self.inventory and self.inventory[item_name] >= quantity:
            self.inventory[item_name] -= quantity
            print(f"Removed {quantity} of {item_name}. Remaining: {self.inventory[item_name]}")
        else:
            print(f"Error: Insufficient stock for {item_name}")

    def check_inventory(self):
        print("\n--- Current Inventory ---")
        if not self.inventory:
            print("Inventory is empty.")
        for item, qty in self.inventory.items():
            print(f"{item}: {qty}")
        print("------------------------\n")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def financial_menu():
    while True:
        print("\n--- Financial Calculations ---")
        print("1. Profit Margin")
        print("2. ROI")
        print("3. Break-even Point")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            rev = get_float_input("Enter Revenue: ")
            cost = get_float_input("Enter Cost: ")
            print(f"Profit Margin: {calculate_profit_margin(rev, cost):.2f}%")
        elif choice == '2':
            gain = get_float_input("Enter Gain from Investment: ")
            cost = get_float_input("Enter Cost of Investment: ")
            print(f"ROI: {calculate_roi(gain, cost):.2f}%")
        elif choice == '3':
            fixed = get_float_input("Enter Fixed Costs: ")
            price = get_float_input("Enter Price per Unit: ")
            var_cost = get_float_input("Enter Variable Cost per Unit: ")
            print(f"Break-even Point: {calculate_break_even_point(fixed, price, var_cost):.2f} units")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def inventory_menu(sm):
    while True:
        print("\n--- Stock Management ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Check Inventory")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Enter Item Name: ")
            qty = int(get_float_input("Enter Quantity: "))
            sm.add_stock(name, qty)
        elif choice == '2':
            name = input("Enter Item Name: ")
            qty = int(get_float_input("Enter Quantity: "))
            sm.remove_stock(name, qty)
        elif choice == '3':
            sm.check_inventory()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def main():
    sm = StockManager()
    while True:
        print("\n=== Business Management Tools ===")
        print("1. Financial Calculations")
        print("2. Stock Management")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            financial_menu()
        elif choice == '2':
            inventory_menu(sm)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
