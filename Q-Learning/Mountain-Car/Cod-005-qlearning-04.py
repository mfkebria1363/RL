import time
import gym
import numpy as np


def randState(x_min = -0.8, x_max= 0.35, v_min = 0, v_max = 0.02):
    x = np.random.uniform() * (x_max - x_min) + x_min
    v = np.random.uniform() * (v_max - v_min) + v_min
    return np.array([x, v])

def stateToIndex (state, xAl = 10, vAl = 100):
    x = int((state[0] - env.observation_space.low[0]) * xAl)  
    v = int((state[1] - env.observation_space.low[1]) * vAl)
    return x, v

def shape(env, xAl = 10, vAl = 100):
    dims = env.observation_space.high - env.observation_space.low
    x = int(dims[0] * xAl) 
    v = int(dims[1] * vAl) 
    a = env.action_space.n
    return x, v, a

def parameters():
    num_episodes = 1000
    max_try = 1000
    
    learning_rate = 0.05
    discount_rate = 0.99 
    explorationTrheshold = 0.95
    return num_episodes, max_try, learning_rate, discount_rate, explorationTrheshold

def rewardFunction(prvState, nextState):
    vChange = nextState[1] - prvState[1]
    reward = - 1
    isDone = False
    if (nextState[0] > 0.45):
        isDone = True
        reward = 1000

    return reward, isDone 

def explorationTrheshold(e, E):
    min_th = 0.25
    max_th = 0.75
    return max_th - e / E * (max_th - min_th)

env = gym.make('MountainCar-v0')
env = env.unwrapped

Q_table = np.zeros(shape(env))
n_ep, mx_tr, lr, dr, et = parameters()

print (shape(env))


for ep in range(n_ep):
    env.reset()

    if ep % 25 == 0:
        print ("Episode: ", ep)

    done = False
    counter = 0
    while  counter < mx_tr and not done: 

        counter += 1
        #lr = max(1 / (counter + 1), 0.01)
        lr = 0.05
        epcilon = np.random.uniform()
        thr = explorationTrheshold(ep, n_ep)

        if epcilon < thr:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q_table[stateToIndex(env.state)])

        crntState = env.state
        new_state, reward, done, info = env.step(action)

        reward, done = rewardFunction(crntState, new_state)
        # env.render()

        if (done):
            print ("Well done!")

        cs = stateToIndex(crntState)
        ns = stateToIndex(new_state)
        old_Q = Q_table[cs][action]
        next_Q = np.max(Q_table[ns])
        Q_table[cs][action] = old_Q + lr * ( reward + dr * next_Q - old_Q)
        
    if (ep % 100 == 0 and ep > 0):
        name = "Q-Learning/Mountain-Car/Qtable_{}.txt".format(ep) 
        np.savetxt(name, Q_table.reshape(1, -1))

np.savetxt("Q-Learning/Mountain-Car/Qtable_final.txt", Q_table.reshape(1, -1))









