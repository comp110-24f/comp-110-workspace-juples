"""My first exercise in COMP110!"""

__author__ = "730511752"


def mimic(message: str) -> str:
    """This message will return the message you input"""
    return message


def main() -> None:
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
