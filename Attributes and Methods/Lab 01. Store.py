class Store:

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items ={}


    @classmethod
    def from_size (cls, name, type, size):
        cap = 0.5 * size
        return Store(name, type, cap)


    def add_item (self, name):
        if name not in self.items.keys():
            self.items[name] = 1
            return f"{name} added to the store"
        if self.items[name] and self.items[name]<self.capacity:
            self.items[name]+=1
        elif  self.items[name] and self.items[name]>=self.capacity:
            return "Not enough capacity in the store"


    def remove_item (self, name, amount):
        if name in self.items.keys():
            if self.items[name]>=amount:
                self.items[name] -=amount
                return f"{amount} {name} removed from the store"
        return f"Cannot remove {amount} {name}"


    def __repr__(self) :
        return f"{self.name} of type {self.type} with capacity {self.capacity:.0f}"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
