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
    
    return [(x,y), (x1, y1), (x2, y2)]

def check_allsnake(x, y, snake):
    for position in snake:
        if position == (x,y):
            return False
    return True

def check_allapple(x, y, apples):
    # apples = {"green": [pos1, pos2], "red": pos3}
    # On aplatit tout en une liste de positions a comparer
    all_apple_positions = apples["green"] + [apples["red"]]
    return (x, y) not in all_apple_positions

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = spawn_snake(width)

        self.apple = {
            "green": [None, None],
            "red": None,
        }
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
            return False, -100
        
        if (not check_allapple(x, y, apple)):
            self.snake.insert(0, (x,y))
            if ((x,y) == apple["red"]):
                self.snake.pop()
                self.snake.pop()
                if (len(self.snake) <= 0):
                    return False, -150
                apple["red"] = self.spawn_apple(size)
                return True, -50
            else:
                if ((x,y) == apple["green"][0]):
                    apple["green"][0] = self.spawn_apple(size)
                else:
                    apple["green"][1] = self.spawn_apple(size)
                return True, 100
        else:
            self.snake.pop()
            if (not check_allsnake(x, y, self.snake)):
                return False, -100
            self.snake.insert(0, (x,y))
            return True, -10

    def visualizer(self):
        grille = [
            [
                "W" if x in (0, self.width + 1) or y in (0, self.height + 1) else "."
                for x in range(self.width + 2)
            ]
            for y in range(self.height + 2)
        ]

        for x, y in self.snake:
            grille[y + 1][x + 1] = "S"

        x, y = self.snake[0]
        grille[y + 1][x] = "H"
    
        for x, y in self.apple["green"]:
            grille[y][x] = "G"

        x, y = self.apple["red"]
        grille[y][x] = "R"

        for ligne in grille:
            print(" ".join(ligne))
        return grille

    def get_vision(self):
        x, y = self.snake[0]
        grille = self.visualizer()

        left = grille[y][x-1] if x > 0 else "W"
        right = grille[y][x+1] if x < self.width - 1 else "W"
        up = grille[y-1][x] if y > 0 else "W"
        down = grille[y+1][x] if y < self.height - 1 else "W"
        return left, right, up, down



        
        

def afficher(self):
    grille = [["." for _ in range(board.width)] for _ in range(board.height)]

    for x, y in board.snake:
        grille[y][x] = "S"

    for x, y in board.apple["green"]:
        grille[y][x] = "G"

    x, y = board.apple["red"]
    grille[y][x] = "R"

    for ligne in grille:
        print(" ".join(ligne))

board = Board(10, 10)
board.afficher()