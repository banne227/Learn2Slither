from snake import (
    check_allapple,
    check_allsnake,
    generate_number,
    simplificated_state,
    spawn_snake,
)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = spawn_snake(width)

        self.apple = {
            "green": [None, None],
            "red": None,
        }
        self.alive = True
        self.init_apple(width)

    def spawn_apple(self, size):
        while True:
            x = generate_number(size)
            y = generate_number(size)

            if (check_allsnake(x, y, self.snake)
                    and check_allapple(x, y, self.apple)):
                return (x, y)

    def init_apple(self, size):
        self.apple["green"] = [self.spawn_apple(size)]
        self.apple["green"].append(self.spawn_apple(size))
        self.apple["red"] = self.spawn_apple(size)

    def step(self, action, size):
        apple = self.apple
        x, y = self.snake[0]
        dx, dy = action
        x, y = x + dx, y + dy

        if x < 0 or x >= size or y < 0 or y >= size:
            self.alive = False
            print("Game Over: Snake hit the wall.")
            return -100

        if (not check_allapple(x, y, apple)):
            self.snake.insert(0, (x, y))
            if ((x, y) == apple["red"]):
                self.snake.pop()
                self.snake.pop()
                if (len(self.snake) <= 0):
                    self.alive = False
                    print("Game Over: Snake has no body left "
                          "after eating red apple.")
                    return -150
                apple["red"] = self.spawn_apple(size)
                return -50
            else:
                if ((x, y) == apple["green"][0]):
                    apple["green"][0] = self.spawn_apple(size)
                else:
                    apple["green"][1] = self.spawn_apple(size)
                return 100
        else:
            self.snake.pop()
            if (not check_allsnake(x, y, self.snake)):
                self.alive = False
                print("Game Over: Snake collided with itself.")
                return -100
            self.snake.insert(0, (x, y))
            return -10

    def get_grid(self):
        grille = [
            [
                "W" if x in (0, self.width + 1) or y in (0, self.height + 1)
                else "." for x in range(self.width + 2)
            ]
            for y in range(self.height + 2)
        ]

        for x, y in self.snake:
            grille[y + 1][x + 1] = "S"

        x, y = self.snake[0]
        grille[y + 1][x + 1] = "H"

        for x, y in self.apple["green"]:
            grille[y + 1][x + 1] = "G"

        x, y = self.apple["red"]
        grille[y + 1][x + 1] = "R"
        return grille

    def visualizer(self):
        grille = self.get_grid()

        for ligne in grille:
            print(" ".join(ligne))
        return grille

    def watch(self, grille, x, y, dx, dy):
        vision = []
        x += dx
        y += dy
        while grille[y][x] != "W":
            vision.append(grille[y][x])
            x += dx
            y += dy
        vision.append("W")
        return vision

    def get_vision(self):
        if len(self.snake) <= 1:
            return None

        x, y = self.snake[0]
        grille = self.get_grid()

        x += 1
        y += 1

        left = self.watch(grille, x, y, -1, 0)
        right = self.watch(grille, x, y, 1, 0)
        up = self.watch(grille, x, y, 0, -1)
        down = self.watch(grille, x, y, 0, 1)

        return simplificated_state(left, right, up, down)

    def is_alive(self):
        return self.alive

    def score(self):
        return len(self.snake)
