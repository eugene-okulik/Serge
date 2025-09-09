class Flower:
    def __init__(self, name, color, stem_length, freshness, price, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.price = price
        self.lifespan = lifespan

    def __repr__(self):
        return f"{self.name}({self.color}, {self.price}р)"


class Rose(Flower):
    def __init__(self, color="красный", stem_length=40, freshness=1):
        super().__init__("Роза", color, stem_length, freshness, price=150, lifespan=7)


class Tulip(Flower):
    def __init__(self, color="желтый", stem_length=30, freshness=2):
        super().__init__("Тюльпан", color, stem_length, freshness, price=100, lifespan=5)


class Lily(Flower):
    def __init__(self, color="белый", stem_length=50, freshness=1):
        super().__init__("Лилия", color, stem_length, freshness, price=200, lifespan=10)


class Bouquet:
    def __init__(self, flowers=None):
        self.flowers = flowers if flowers else []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def cost(self):
        return sum(f.price for f in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(f.lifespan for f in self.flowers) / len(self.flowers)

    def sort_by(self, attribute):

        self.flowers.sort(key=lambda f: getattr(f, attribute))

    def find(self, condition):
        return [f for f in self.flowers if condition(f)]

    def find_by_average_lifespan(self, tolerance=0):
        avg = self.average_lifespan()
        return self.find(lambda f: abs(f.lifespan - avg) <= tolerance)

    def __repr__(self):
        return f"Букет: {self.flowers}"


rose = Rose()
tulip = Tulip()
lily = Lily()
bouquet = Bouquet([rose, tulip, lily])

print(bouquet)
print(bouquet.cost())

bouquet.sort_by("stem_length")
print(bouquet)

print(bouquet.average_lifespan())

print(bouquet.find(lambda f: f.color == "белый"))

print(bouquet.find_by_average_lifespan(3))
