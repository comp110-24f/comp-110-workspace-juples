__author__: str = "730511752"


def main_planner(guests: int) -> None:
    """this function is here to call the other functions and present the information"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


# needed some help to understand how to space up my $ with the rest of my output


def tea_bags(people: int) -> int:
    """This function returns the amount of tea bags required for the party"""
    return 2 * people


def treats(people: int) -> int:
    """this function calculates the amount of treats"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """this function calculates the cost of both treats and teas"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
