import random


def generate_number(size):
    return random.randint(0, size - 1)


def generate_body(x, y):
    direction = random.choice([
        (0, 1),   # haut
        (0, -1),  # bas
        (-1, 0),  # gauche
        (1, 0)    # droite
    ])

    dx, dy = direction
    return x + dx, y + dy


def spawn_snake(size):
    x = generate_number(size)
    y = generate_number(size)

    while True:
        x1, y1 = generate_body(x, y)
        if 0 <= x1 < size and 0 <= y1 < size:
            break

    while True:
        x2, y2 = generate_body(x1, y1)
        if (0 <= x2 < size and 0 <= y2 < size and (x2, y2) != (x, y)):
            break

    return [(x, y), (x1, y1), (x2, y2)]


def check_allsnake(x, y, snake):
    for position in snake:
        if position == (x, y):
            return False
    return True


def check_allapple(x, y, apples):
    # apples = {"green": [pos1, pos2], "red": pos3}
    # On aplatit tout en une liste de positions a comparer
    all_apple_positions = apples["green"] + [apples["red"]]
    return (x, y) not in all_apple_positions


def get_one_state(direction):
    if direction[0] == "W" or direction[0] == "S":
        return "D"  # danger
    else:
        for element in direction:
            if element is not None and element != "W" and element != ".":
                return element
    return "E"  # empty


def simplificated_state(left, right, up, down):
    return " ".join([
        get_one_state(left), get_one_state(right),
        get_one_state(up), get_one_state(down)
    ])
