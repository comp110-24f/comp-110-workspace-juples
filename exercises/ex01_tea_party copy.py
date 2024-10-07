__author__: str = "730511752"


def main_planner(guests: int) -> None:
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost:", "$", cost(tea_count=tea_bags(guests), treat_count=treats(guests)))


def tea_bags(people: int) -> int:
    """This function returns the amount of tea bags required for the party"""
    return 2 * people


def treats(people: int) -> int:
    """this function calculates the amount of treats"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """this function calculates the cost of both treats and teas"""
    return tea_count * 0.5 + treat_count * 0.75
