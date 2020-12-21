class Food:
    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens

    @staticmethod
    def parse(line):
        ingredients, allergens = line[:-1].split(' (contains ')
        return Food(ingredients.split(' '), allergens.split(', '))


def parse_foods(data):
    return list(map(Food.parse, data.strip().split('\n')))


def build_index(foods):
    index = {}
    for food in foods:
        for allergen in food.allergens:
            if allergen in index:
                index[allergen] = index[allergen].intersection(food.ingredients)
            else:
                index[allergen] = set(food.ingredients)
    return index


def part1(data):
    foods = parse_foods(data)
    index = build_index(foods)
    dangerous_ingredients = set.union(*index.values())
    print(dangerous_ingredients)
    ans = 0
    for food in foods:
        for ingredient in food.ingredients:
            ans += ingredient not in dangerous_ingredients
    return ans


def part2(data):
    foods = parse_foods(data)
    index = build_index(foods)
    matching = {}
    for _ in range(len(index)):
        for allergen, ingredients in index.items():
            if len(ingredients) == 1:
                matching[allergen] = ingredient_to_remove = next(iter(ingredients))
                for ingredients in index.values():
                    if ingredient_to_remove in ingredients:
                        ingredients.remove(ingredient_to_remove)
                break
    dangerous_ingredients = [ingredient for _, ingredient in sorted(matching.items())]
    return ','.join(dangerous_ingredients)
