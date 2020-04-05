import sys
import time
import numpy as np
import pandas as pd

if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

UNIT = 100
MAZE_H = 4
MAZE_W = 4
HALF_UNIT = UNIT / 2
HALF_UNIT_MINUS10 = HALF_UNIT - 10
SIZE = int(3 * UNIT / 8)
ROUND = 3
TEXT_SIZE = 7


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_W * UNIT, MAZE_H * UNIT))
        self.action_space = ["Haut", "Bas", "Gauche", "Droite"]
        self.n_actions = len(self.action_space)
        self.q_table = pd.DataFrame(columns=self.action_space, dtype=np.float64)
        self._build_maze()
        self.textList = []

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white', height=MAZE_H * UNIT, width=MAZE_W * UNIT)
        # Create grids
        for c in range(1, MAZE_W):
            x0, y0 = c * UNIT, 0
            x1, y1 = x0, y0 + MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)

        for r in range(1, MAZE_H):
            x0, y0 = 0, r * UNIT
            x1, y1 = x0 + MAZE_W * UNIT, y0
            self.canvas.create_line(x0, y0, x1, y1)

        # Creer le point de départ de carre ou de rond
        pointDepart = np.array([UNIT / 8, UNIT / 8])

        x0, y0 = pointDepart[0] + 0 * UNIT, pointDepart[1] + 0 * UNIT
        x1, y1 = x0 + 3 * UNIT / 4, y0 + 3 * UNIT / 4
        self.agent = self.canvas.create_rectangle(x0, y0, x1, y1, fill='red')

        x0, y0 = pointDepart[0] + (MAZE_W - 2) * UNIT, pointDepart[1] + (MAZE_H - 2) * UNIT
        x1, y1 = x0 + 3 * UNIT / 4, y0 + 3 * UNIT / 4
        self.treasure = self.canvas.create_oval(x0, y0, x1, y1, fill="yellow")

        x0, y0 = pointDepart[0] + (MAZE_W - 2) * UNIT, pointDepart[1] + (MAZE_H - 3) * UNIT
        x1, y1 = x0 + 3 * UNIT / 4, y0 + 3 * UNIT / 4
        self.trap1 = self.canvas.create_rectangle(x0, y0, x1, y1, fill='black')

        x0, y0 = pointDepart[0] + (MAZE_W - 3) * UNIT, pointDepart[1] + (MAZE_H - 2) * UNIT
        x1, y1 = x0 + 3 * UNIT / 4, y0 + 3 * UNIT / 4
        self.trap2 = self.canvas.create_rectangle(x0, y0, x1, y1, fill='black')

        self.canvas.pack()
        return self.agent, self.treasure, self.trap1, self.trap2

    def step(self, action):
        s = self.canvas.coords(self.agent)
        base_action = np.array([0, 0])
        if action == 'Haut':  # Go UP
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 'Bas':  # Go DOWN
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 'Gauche':  # Go LEFT
            if s[0] > UNIT:
                base_action[0] -= UNIT
        elif action == 'Droite':  # Go RIGHT
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        self.canvas.move(self.agent, base_action[0], base_action[1])

    def check_state_exist(self):
        s = str(self.canvas.coords(self.agent))
        if s not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.action_space),
                    index=self.q_table.columns,
                    name=s
                )
            )

    def render(self):
        time.sleep(0.02)
        self.update()

    def choose_action(self):
        s = str(self.canvas.coords(self.agent))
        if np.random.uniform() < 0.1:
            action = np.random.choice(self.action_space)
        else:
            actionScores = self.q_table.loc[s, :]
            action = np.random.choice(actionScores[actionScores == np.max(actionScores)].index)
        return action

    def learn(self, etatActuel, action, etatSuivant):
        self.check_state_exist()
        if etatSuivant == self.canvas.coords(self.treasure):
            q_cible = 1
        elif etatSuivant == self.canvas.coords(self.trap1) or etatSuivant == self.canvas.coords(self.trap2):
            q_cible = -1
        else:
            actionScores = self.q_table.loc[str(etatSuivant), :]
            q_cible = 0.9 * np.max(actionScores)
        q_actuel = self.q_table.loc[str(etatActuel), action]
        self.q_table.loc[str(etatActuel), action] += 0.1 * (q_cible - q_actuel)

    def reset(self):
        self.update()
        time.sleep(0.25)
        self.canvas.delete(self.agent)
        pointDepart = np.array([UNIT / 8, UNIT / 8])
        x0, y0 = pointDepart[0], pointDepart[1]
        x1, y1 = x0 + 3 * UNIT / 4, y0 + 3 * UNIT / 4
        self.agent = self.canvas.create_rectangle(x0, y0, x1, y1, fill="red")

    def writeText(self, text, pos):
        element = self.canvas.create_text(float(pos[0]) + 35, float(pos[3]) + 8, text=text, font=('Times', TEXT_SIZE))
        self.textList.append(element)

    def resetText(self):
        for text in self.textList:
            self.canvas.delete(text, tk.END)


def displayScore():
    env.resetText()
    for index, row in env.q_table.iterrows():
        rows = round(row['Haut'], ROUND), round(row['Bas'], ROUND), round(row['Gauche'], ROUND), round(row['Droite'],
                                                                                                       ROUND)
        pos = (index.replace('[', '').replace(']', '').split(','))
        env.textList.append(env.writeText(rows, pos))


def update():
    input("Press enter to start")
    env.check_state_exist()
    counter = 0
    while counter <= 100:
        env.render()
        etatActuel = env.canvas.coords(env.agent)
        choice = env.choose_action()
        env.step(choice)
        etatSuivant = env.canvas.coords(env.agent)
        print(choice)
        env.learn(etatActuel, choice, etatSuivant)
        if etatSuivant == env.canvas.coords(env.treasure):
            displayScore()
            env.reset()
            counter = counter + 1
        elif etatSuivant == env.canvas.coords(env.trap1) or etatSuivant == env.canvas.coords(env.trap2):
            env.resetText()
            displayScore()
            env.reset()
    print(env.q_table)
    input("Press enter to terminate")
    env.destroy()


if __name__ == "__main__":
    env = Maze()
    update()
    env.mainloop()
