import random


class Gridworld():
    def __init__(self):
        self.x = 0  # row
        self.y = 0  # column

    def step(self, a):
        # 0: right, 1: left, 2: up, 3:down
        if a == 0:
            self.move_right()
        elif a == 1:
            self.move_left()
        elif a == 2:
            self.move_up()
        elif a == 3:
            self.move_down()

        reward = -1
        done = self.is_done()
        return (self.x, self.y), reward, done

    def move_right(self):
        self.y += 1
        if self.y > 3:
            self.y = 3

    def move_left(self):
        self.y -= 1
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.x += 1
        if self.x > 3:
            self.x = 3

    def move_up(self):
        self.x -= 1
        if self.x < 0:
            self.x = 0

    def is_done(self):
        if self.x == 3 and self.y == 3:
            return True
        else:
            return False

    def get_state(self):
        return self.x, self.y

    def reset(self):
        self.x = 0
        self.y = 0
        return self.x, self.y


class Agent():
    def __init__(self):
        pass

    def select_action(self):
        coin = random.random()

        if coin < 0.25:
            action = 0
        elif coin < 0.5:
            action = 1
        elif coin < 0.75:
            action = 2
        else:
            action = 3

        return action


def main():
    env = Gridworld()
    agent = Agent()
    data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # value
    gamma = 1.0
    alpha = 0.0001

    for k in range(50000):
        done = False
        history = []

        while not done:
            action = agent.select_action()
            (x, y), reward, done = env.step(action)
            history.append((x, y, reward))

        env.reset()

        cum_reward = 0  # G_T = 0
        for transition in history[::-1]:  # backward
            x, y, reward = transition
            data[x][y] = data[x][y] + alpha*(cum_reward - data[x][y])
            cum_reward = reward + gamma*cum_reward

    for row in data:
        print(row)

if __name__ == '__main__':
    main()
