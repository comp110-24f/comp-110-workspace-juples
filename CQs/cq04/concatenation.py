def concat(word1: str, word2: str) -> str:
    conword = word1 + word2
    conword = f"'{conword}'"
    return conword


word1: str = "happy"
word2: str = "tuesday"
print(concat(word1, word2))

if __name__ == "__main__":
    concat(word1, word2)
