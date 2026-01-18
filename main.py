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
        for item, qty in self.inventory.items():
            print(f"{item}: {qty}")
        print("------------------------\n")

def main():
    print("Welcome to Business Management Tools")
    
    # Financial Calculations Demo
    rev = 1000
    cost = 700
    print(f"Profit Margin for Revenue {rev} and Cost {cost}: {calculate_profit_margin(rev, cost):.2f}%")
    
    # Stock Management Demo
    sm = StockManager()
    sm.add_stock("Widget A", 50)
    sm.add_stock("Gadget B", 30)
    sm.check_inventory()
    sm.remove_stock("Widget A", 10)
    sm.check_inventory()

if __name__ == "__main__":
    main()
