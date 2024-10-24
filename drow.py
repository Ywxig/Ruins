def drow(map_ : list, hero_pos : tuple) -> None:
    M = map_
    M[hero_pos[1]][hero_pos[0]] = "@"
    arr = []
    for i in M:
        arr.append("".join(i))
    print("\n".join(arr))
