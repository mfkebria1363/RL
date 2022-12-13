import gym
import numpy as np

env = gym.make('FrozenLake-v0')
env = env.unwrapped
nA = env.action_space.n
nS = env.observation_space.n

def eval_state_action(V, s, a, gamma=0.99):
    return np.sum([p * (rew + gamma*V[next_s]) for p, next_s, rew, _ in env.P[s][a]])

def value_iteration(eps=0.0001):
    V = np.zeros(nS)
    it = 0
    while True:
        delta = 0
        # update the value for each state
        for s in range(nS):
            old_v = V[s]
            V[s] = np.max([eval_state_action(V, s, a) for a in range(nA)])
            # equation 3.10
            delta = max(delta, np.abs(old_v - V[s]))
        # if stable, break the cycle
        if delta < eps:
            break
        else:
            print('Iter:', it, ' delta:', np.round(delta,5))
        it += 1
    return V

def run_episodes(env, V, num_games=100):
    tot_rew = 0
    state = env.reset()
    for _ in range(num_games):
        done = False
        while not done:
            # choose the best action using the value function
            action = np.argmax([eval_state_action(V, state, a) for a in range(nA)]) #(11)
            next_state, reward, done, _ = env.step(action)
            state = next_state
            tot_rew += reward
            if done:
                state = env.reset()
    print('Won %i of %i games!'%(tot_rew, num_games))

V = value_iteration(eps=0.0001)

run_episodes(env, V, 100)

