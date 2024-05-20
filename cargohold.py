class Item:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    def __str__(self):
        return f"{self._name} {self._weight}"


class Suitcase:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []
        self.items_weight = 0

    def add_item(self, item: Item):
        if item.weight + self.items_weight <= self.max_weight:
            self.items.append(item)
            self.items_weight += item.weight

    def __str__(self):
        return f"{len(self.items)}({self.items_weight}kg)"


book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

suitcase = Suitcase(5)
print(suitcase)

suitcase.add_item(book)
print(suitcase)

suitcase.add_item(phone)
print(suitcase)

suitcase.add_item(brick)
print(suitcase)
