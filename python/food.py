class Food:
    base_hearts = 1

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingredients=[])
        food.hearts = hearts
        return food


def main():
    mushroom_skewers = Food(ingredients=["Mushrooms", "Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewers.hearts} hearts!")

    mushroom_skewers = Food.from_nothing(hearts=2)
    print(f"This skewer heals {mushroom_skewers.hearts} hearts!")


main()
