# 🐍 Learn2Slither

> Reinforcement Learning project where an autonomous Snake learns to survive using **Q-Learning**.

## 📖 Overview

Learn2Slither is an Artificial Intelligence project based on **Reinforcement Learning**.

The objective is to train a Snake agent capable of making decisions through **trial and error**. The agent interacts with its environment, receives rewards or penalties depending on its actions, and progressively improves its behavior using the **Q-Learning** algorithm.

The project follows the specifications provided by the subject and includes a **graphical visualization** of the board during execution.

---

## ✨ Features

- ✅ 10x10 game board
- ✅ Snake starts with a length of 3
- ✅ Two green apples
- ✅ One red apple
- ✅ Random board generation
- ✅ Q-Learning implementation (Q-Table)
- ✅ Reward system
- ✅ Multiple training sessions
- ✅ Save trained models
- ✅ Load existing models
- ✅ Learning can be disabled for evaluation
- ✅ Step-by-step execution mode
- ✅ Graphical visualization (bonus)

---

## 🧠 Reinforcement Learning

The Snake learns using the **Q-Learning** algorithm.

For every state, the agent:

1. Observes its environment.
2. Chooses one of the four possible actions:
   - Up
   - Down
   - Left
   - Right
3. Receives a reward.
4. Updates its Q-Table.
5. Repeats the process over thousands of training sessions.

The exploration/exploitation strategy allows the agent to progressively discover better actions and improve its survival rate.

---

## 🎮 Game Rules

- Board size: **10 × 10**
- Snake starts with **3 cells**
- 2 Green Apples
- 1 Red Apple

### Green Apple

- Increases the snake length by **1**
- Spawns a new green apple

### Red Apple

- Decreases the snake length by **1**
- Spawns a new red apple

### Game Over

The game ends when:

- the snake hits a wall
- the snake collides with itself
- the snake length reaches 0

---

## 👀 Snake Vision

The agent only has access to its **local vision** as required by the project specification.

It can observe information only in the four directions from its head.

The AI does **not** have access to the complete board.

---

## 🖥️ Graphical Display

This project includes the **visualization bonus**.

A graphical window displays:

- the board
- the snake
- green apples
- red apples

⚠️ No configuration menu or lobby has been implemented.
The bonus consists only of the real-time visual rendering of the game.

The display can also be disabled to speed up training.

---

# 🚀 Usage

## Run the project

```bash
python main.py
```

---

## Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `-sessions` | Number of training sessions | `1` |
| `-save` | Save the trained model | `None` |
| `-load` | Load an existing model | `None` |
| `-visual` | Enable or disable graphical display (`on` / `off`) | `on` |
| `-dontlearn` | Disable learning (evaluation mode) | `False` |
| `-step-by-step` | Execute one move at a time | `False` |

---

## Examples

Train the AI for 100 sessions:

```bash
python main.py -sessions 100
```

Train and save the model:

```bash
python main.py -sessions 1000 -save models/model1000.pkl
```

Load a model:

```bash
python main.py -load models/model1000.pkl
```

Evaluate a trained model without learning:

```bash
python main.py -load models/model1000.pkl -dontlearn
```

Fast training without graphics:

```bash
python main.py -sessions 10000 -visual off
```

Step-by-step visualization:

```bash
python main.py -load models/model1000.pkl -step-by-step
```

---

# 📂 Project Structure

```
.
├── models/
│   ├── model_1
│   ├── model_10
│   └── model_100
├── ...
├── main.py
└── README.md
```

---

# 💾 Models

The project supports exporting and importing trained models.

Saved models contain the learned Q-values, allowing the AI to resume training or be evaluated without modifying its knowledge.

---

# ⚙️ Technologies

- Python 3
- Q-Learning
- argparse
- Graphical rendering library (depending on your implementation)

---

# 🎯 Objectives

The agent should learn to:

- survive as long as possible
- avoid walls
- avoid colliding with itself
- prioritize green apples
- avoid red apples
- reach a snake length of **10 or more**

---

# 📸 Bonus

Implemented bonus:

---

# 👨‍💻 Author

Project developed as part of the **Learn2Slither** Reinforcement Learning project.
