from dis import disco
import time
import gym
import numpy as np

def stateToIndex (state, xAl = 10, vAl = 100):
    x = int((state[0] - env.observation_space.low[0]) * xAl)  
    v = int((state[1] - env.observation_space.low[1]) * vAl)
    return x, v

def shape(env, xAl = 10, vAL = 100):
    dims = env.observation_space.high - env.observation_space.low
    x = int(dims[0] * xAl) + 1
    y = int(dims[1] * vAL) + 1
    z = env.action_space.n
    return x, y, z

def parameters():
    num_episodes = 500
    max_try = 100

    learning_rate = 0.05
    discount_rate = 0.99
    explorationTrheshold = 0.05
    return num_episodes, max_try, learning_rate, discount_rate, explorationTrheshold

def rewardFunction(prvState, nextState):
    vChange = nextState[1] - prvState[1]
    reward = vChange - 0.5
    isDone = False
    if (nextState[0] > 0.45):
        isDone = True
        reward = 1000

    return reward, isDone 

env = gym.make('MountainCar-v0')
env = env.unwrapped

Q_table = np.loadtxt("Q-Learning/Mountain-Car/Qtable_final.txt").reshape(18, 14, -1)

for  i in range(100):
    done = False
    total_reward = 0
    done = False
    state = env.reset()

    while not done:
        act = np.argmax(Q_table[stateToIndex(env.state)])
        new_state, reward, done, info = env.step(act)
        reward, done = rewardFunction(state, new_state)
        total_reward += reward
        state = new_state
        env.render()

    print (total_reward)
    time.sleep(1)

