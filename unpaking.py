for coords in [(1, 2), (2, 5), (7, 12), (8, 2)]:
    x = coords[0]
    y = coords[1]
    print(f"Мы на клетке [{x}, {y}]")

for coords in [(1, 2), (2, 5), (7, 12), (8, 2)]:
    x, y = coords
    print(f"Мы на клетке [{x}, {y}]")

for x, y in [(1, 2), (2, 5), (7, 12), (8, 2)]:
    print(f"Мы на клетке [{x}, {y}]")

for name, (x, y) in [
    ("кролик", (1, 2)),
    ("сова", (2, 5)),
    ("утка", (7, 12)),
    ("лягушка", (8, 2))
    ]:
    print(f"{name} на клетке {x}, {y}")

for i, name in enumerate(["кролик", "сова", "утка", "лягушка"]):
    print(f"Животное номер {i}: {name}")