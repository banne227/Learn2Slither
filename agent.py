import pygame
import time
from board import Board
from ui import draw_board, CELL_SIZE
from qlearning import choose_action, update_q
from qlearning import action_to_delta, load_model, save_model


def run(
    nb_sessions, load_path, save_path,
    dont_learn, visual, step_by_step, speed
):

    Q = load_model(load_path) if load_path else {}
    epsilon = 0.01 if dont_learn else 0.9  # exploitation pure si dont_learn
    when, max_score = 0, 0

    # print("Q table at start:", Q)

    if visual == "on":
        pygame.init()
        screen = pygame.display.set_mode((12 * CELL_SIZE, 12 * CELL_SIZE))

    for session in range(nb_sessions):
        board = Board(10, 10)
        state = board.get_vision()
        print(f"Session {session + 1}/{nb_sessions}")

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
                update_q(
                    Q,
                    state,
                    action,
                    reward,
                    next_state,
                    alpha=0.1,
                    gamma=0.9,
                )

            state = next_state

            if visual == "on":
                if step_by_step:
                    input("Appuie sur Entrée pour continuer...")
                else:
                    time.sleep(speed)

            if board.score() > max_score:
                when = session
                max_score = board.score()
        epsilon = max(0.05, epsilon * 0.995)

    print(
        f"Meilleur score atteint : {max_score} "
        f"à la session {when + 1}/{nb_sessions}"
    )

    if save_path:
        save_model(Q, save_path)
