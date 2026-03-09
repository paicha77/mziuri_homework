class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def show_items(self):
        print(self.items)


cart = Cart()
cart.add_item("Apple")
cart.add_item("Bread")
cart.remove_item("Apple")
cart.show_items()