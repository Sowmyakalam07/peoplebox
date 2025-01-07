class OrderService:
    def __init__(self, stock):
        self.stock = stock

    def validateOrder(self, order):
        for item, quantity in order.items():
            if item not in self.stock:
                print(f"Error: Item '{item}' is not in stock.")
                return False
            if self.stock[item]['quantity'] < quantity:
                print(f"Error: Insufficient stock for item '{item}'. Requested: {quantity}, Available: {self.stock[item]['quantity']}.")
                return False
        return True

    def calculateTotal(self, order):
        subtotal = sum(self.stock[item]['price'] * quantity for item, quantity in order.items())
        tax = subtotal * 0.10  # 10% tax
        discount = 0.05 * subtotal if subtotal > 100 else 0  # 5% discount for orders above $100
        total = subtotal + tax - discount
        return subtotal, tax, discount, total

    def processOrder(self, order):
        # Validate the order
        is_valid = self.validateOrder(order)
        if not is_valid:
            return "Order validation failed. Please correct the issues and try again."

        # Calculate totals
        subtotal, tax, discount, total = self.calculateTotal(order)

        # Update stock
        for item, quantity in order.items():
            self.stock[item]['quantity'] -= quantity

        # Generate receipt
        receipt = "Order Receipt\n"
        receipt += "-" * 30 + "\n"
        receipt += "{:<15}{:<10}{:<10}\n".format("Item", "Quantity", "Price")
        for item, quantity in order.items():
            price = self.stock[item]['price'] * quantity
            receipt += f"{item:<15}{quantity:<10}{price:<10.2f}\n"

        receipt += "-" * 30 + "\n"
        receipt += f"Subtotal: ${subtotal:.2f}\n"
        receipt += f"Tax (10%): ${tax:.2f}\n"
        receipt += f"Discount: -${discount:.2f}\n"
        receipt += f"Total: ${total:.2f}\n"
        receipt += "-" * 30 + "\n"
        receipt += "Thank you for your order!"

        return receipt



stock = {
        "apple": {"price": 1.0, "quantity": 50},
        "banana": {"price": 0.5, "quantity": 100},
        "orange": {"price": 0.75, "quantity": 80},
}
print(stock)
# Create the OrderService instance
order_service = OrderService(stock)
order = {
        "apple": 5,
        "banana": 200,  # Example with insufficient stock
        "orange": 8,
    }

# Process the order
receipt = order_service.processOrder(order)
print(receipt)
class OrderService:
    def __init__(self, stock):
        self.stock = stock

    def validateOrder(self, order):
        for item, quantity in order.items():
            if item not in self.stock:
                print(f"Error: Item '{item}' is not in stock.")
                return False
            if self.stock[item]['quantity'] < quantity:
                print(f"Error: Insufficient stock for item '{item}'. Requested: {quantity}, Available: {self.stock[item]['quantity']}.")
                return False
        return True

    def calculateTotal(self, order):
        subtotal = sum(self.stock[item]['price'] * quantity for item, quantity in order.items())
        tax = subtotal * 0.10  # 10% tax
        discount = 0.05 * subtotal if subtotal > 100 else 0  # 5% discount for orders above $100
        total = subtotal + tax - discount
        return subtotal, tax, discount, total

    def processOrder(self, order):
        # Validate the order
        is_valid = self.validateOrder(order)
        if not is_valid:
            return "Order validation failed. Please correct the issues and try again."

        # Calculate totals
        subtotal, tax, discount, total = self.calculateTotal(order)

        # Update stock
        for item, quantity in order.items():
            self.stock[item]['quantity'] -= quantity

        # Generate receipt
        receipt = "Order Receipt\n"
        receipt += "-" * 30 + "\n"
        for item, quantity in order.items():
            price = self.stock[item]['price'] * quantity
            receipt += f"{item} - Quantity: {quantity}, Price: ${price:.2f}\n"

        receipt += "-" * 30 + "\n"
        receipt += f"Subtotal: ${subtotal:.2f}\n"
        receipt += f"Tax (10%): ${tax:.2f}\n"
        receipt += f"Discount: -${discount:.2f}\n"
        receipt += f"Total: ${total:.2f}\n"
        receipt += "-" * 30 + "\n"
        

        return receipt


# Initial stock
stock = {
    "apple": {"price": 1.0, "quantity": 50},
    "banana": {"price": 0.5, "quantity": 100},
    "orange": {"price": 0.75, "quantity": 80},
}
# Display initial stock
print("Available stock at the start:")
for item, details in stock.items():
    print(f"Item: {item}",end=" ")
    print(f"  Price: ${details['price']:.2f}",end=" ")
    print(f"  Quantity: {details['quantity']} units")
    

# Create the OrderService instance
order_service = OrderService(stock)

# Take user input for the order
order = {}
print("\nEnter your order (type 'done' when finished):")
while True:
    item = input("Enter item name: ").strip().lower()
    if not item:  # Handle empty string input
        print("Error: Item name cannot be empty. Please enter a valid item name.")
        continue
    if item == "done":
        break
    if item not in stock:
        print(f"Error: '{item}' is not in stock. Please choose from {list(stock.keys())}.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {item}: "))
        if quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            continue
        order[item] = quantity
    except ValueError:
        print("Error: Please enter a valid integer for quantity.")

# Process the order
if order:
    receipt = order_service.processOrder(order)
    print("\n" + receipt)

    # Display updated stock after the order
    print("\nAvailable stock after order:")
    for item, details in stock.items():
        print(f"Item: {item}",end=" ")
        print(f"  Price: ${details['price']:.2f}",end=" ")
        print(f"  Quantity: {details['quantity']} units")
else:
    print("\nNo items ordered.")
