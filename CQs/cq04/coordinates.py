def get_coords(xs: str, ys: str) -> None:
    index = 0
    while index < len(xs):
        j = 0
        while j < len(ys):
            print((xs[index], ys[j]))
            j += 1
        index += 1
