import random
from board import Board
from model import save_model, load_model

def get_q_values(Q, state):
    if state not in Q:
        Q[state] = {"LEFT": 0.0, "RIGHT": 0.0, "UP": 0.0, "DOWN": 0.0}
    return Q[state]

def choose_action(Q, state, epsilon, actions=["LEFT", "RIGHT", "UP", "DOWN"]):
    if random.random() < epsilon:
        return random.choice(actions)  # Random exploration 
    else:
        q_values = get_q_values(Q, state)
        return max(q_values, key=q_values.get)  # exploitation : choose the action with the highest Q-value

def update_q(Q, state, action, reward, next_state, alpha, gamma):
    q_values = get_q_values(Q, state)
    next_q_values = get_q_values(Q, next_state)
    best_next = max(next_q_values.values())
    q_values[action] = q_values[action] + alpha * (reward + gamma * best_next - q_values[action])

def action_to_delta(action):
    if action == "LEFT":
        return (-1, 0)
    elif action == "RIGHT":
        return (1, 0)
    elif action == "UP":
        return (0, -1)
    elif action == "DOWN":
        return (0, 1)
    else:
        raise ValueError("Invalid action")

#gamma actualisation factor, alpha learning rate, espsilon random exploration factor, dont_learn if True the model will not learn
def train(nb_sessions, dont_learn=False, alpha=0.1, gamma=0.9, epsilon=0.9,load_path=None, save_path=None):
    Q = {}
    if load_path is not None:
        loaded_Q = load_model(load_path)
        if loaded_Q is not None:
            Q = loaded_Q

    for session in range(nb_sessions):
        board = Board(10, 10)
        state = board.get_vision()
        while board.is_alive():
            action = choose_action(Q, state, epsilon)
            reward = board.step(action_to_delta(action), board.width)
            next_state = board.get_vision()
            if not dont_learn:
                update_q(Q, state, action, reward, next_state, alpha, gamma)
            state = next_state
        epsilon = max(0.05, epsilon * 0.995)  # Epsilon reduce after each session 
    if save_path is not None:
        save_model(Q, save_path)
    return Q