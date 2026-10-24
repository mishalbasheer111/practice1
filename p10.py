class Inventory:
    def __init__(self):
        # Maps item name to (quantity, price)
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        return sum(qty * price for qty, price in self.items.values())

    def __len__(self):
        return len(self.items)


inventory = Inventory()

with open("stock.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        if len(parts) != 3:
            print(f"Skipping {parts[0]}: bad line")
            continue

        name = parts[0]
        try:
            qty = int(parts[1])
            price = int(parts[2])
        except ValueError:
            print(f"Skipping {name}: bad number")
            continue

        inventory.add_item(name, qty, price)

print(f"{len(inventory)} items, total value {inventory.total_value()}")

inventory.remove_item("pen")
print(f"{len(inventory)} items, total value {inventory.total_value()}")

try:
    inventory.remove_item("laptop")
except KeyError as error:
    print(f"Error: {error}")
