import numpy as np
import gym

class params:
    def __init__(self, numEpisods, maxTry, learningRate, discountRate):
        self.numEpisods = numEpisods
        self.maxTry = maxTry
        self.learningRate = learningRate
        self.discountRate = discountRate

class Solver:
    def __init__(self, env):
        self.env = env
        self.params = params(100000, 250, 0.01, 0.9)

        self.num_actions = env.action_space.n
        self.accuracy = [10, 10, 10, 10, self.num_actions]
        #self.qTable = np.random.uniform(low=-1, high=1, size=tuple(self.accuracy))
        self.qTable = np.zeros(tuple(self.accuracy))

    def obsrvToState(self, obs):
        idx0 = np.digitize(obs[0], np.linspace(-3.5, 3.5, self.accuracy[0] - 1))
        idx1 = np.digitize(obs[1], np.linspace(-2  , 2  , self.accuracy[1] - 1))
        idx2 = np.digitize(obs[2], np.linspace(-0.4, 0.4, self.accuracy[2] - 1))
        idx3 = np.digitize(obs[3], np.linspace(-3.5, 3.5, self.accuracy[3] - 1))
        return (idx0, idx1, idx2, idx3)

    def explorationTrheshold(self, episod):
        min_th = 0.25
        max_th = 0.75
        return max_th - episod / self.params.numEpisods * (max_th - min_th)

    def selectAction(self, episod, obs):
        if np.random.uniform() < self.explorationTrheshold(episod):
            return env.action_space.sample()
        else:
            return np.argmax(self.qTable[self.obsrvToState(obs )])

    def updateQTable(self, obs, action, reward):
        state = self.obsrvToState(obs)
        oldQ = self.qTable[state][action]
        newQ = np.max(self.qTable[state])
        lr =  self.params.learningRate
        dr =  self.params.discountRate
        self.qTable[state][action] = oldQ + lr * ( reward + dr * newQ - oldQ)

    def playEpisode(self, episodNum):

        totalReward = 0
        crntObs = self.env.reset()

        tryCounter = 0 
        done = False
        while tryCounter < self.params.maxTry and not done:
            action = self.selectAction(episod= episodNum, obs= crntObs)

            new_obs, reward, done, info = env.step(action)
            if done and tryCounter < 199:
                reward = -300

            totalReward += reward
            self.updateQTable(crntObs, action, reward)

            crntObs = new_obs
            #env.render()
        return totalReward

    def learn(self):
        Rewards = []
        totalReward = 0
        for ep in range(self.params.numEpisods):
            Rewards.append(self.playEpisode(ep))
            if (ep % 500 == 0 and ep > 1):
                print (ep ,np.min(Rewards), np.average(Rewards), np.max(Rewards))
                Rewards = []



env = gym.make("CartPole-v1")
solver = Solver(env)

print(env.observation_space.low)

solver.learn()
