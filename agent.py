import pygame   
import time
from board import Board
from ui import draw_board, CELL_SIZE, COLORS
from qlearning import choose_action, update_q, action_to_delta, load_model, save_model

def run(nb_sessions, load_path, save_path, dont_learn, visual, step_by_step, speed=0.1):
    Q = load_model(load_path) if load_path else {}
    epsilon = 0.05 if dont_learn else 0.9  # exploitation pure si dont_learn

    if visual == "on":
        pygame.init()
        screen = pygame.display.set_mode((12 * CELL_SIZE, 12 * CELL_SIZE))  # +2 pour les murs

    for session in range(nb_sessions):
        board = Board(10, 10)
        state = board.get_vision()

        while board.is_alive():
            if visual == "on":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                draw_board(screen, board)

            action = choose_action(Q, state, epsilon)
            reward = board.step(action_to_delta(action), board.width)
            next_state = board.get_vision()

            if not dont_learn:
                update_q(Q, state, action, reward, next_state, alpha=0.1, gamma=0.9)

            state = next_state

            if visual == "on":
                if step_by_step:
                    input("Appuie sur Entrée pour continuer...")
                else:
                    time.sleep(speed)

        epsilon = max(0.05, epsilon * 0.995)

    if save_path:
        save_model(Q, save_path)