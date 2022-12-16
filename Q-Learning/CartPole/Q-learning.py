import numpy as np
import gym

class transformer:
    def __init__(self) -> None:
        self.accuracy =  [20, 20, 20, 20]
        np.linspace(-3.5, 3.5, self.accuracy[0])
        np.linspace(-5  , 5  , self.accuracy[1])
        np.linspace(-0.4, 0.4, self.accuracy[2])
        np.linspace(-5, 5, self.accuracy[3])

    def shape(self, n):
        return [self.accuracy[0], self.accuracy[1], self.accuracy[2], self.accuracy[1], n]

    def transform(self, obs):
        idx0 = np.digitize(obs[0], np.linspace(-3.5, 3.5, self.accuracy[0] - 1))
        idx1 = np.digitize(obs[1], np.linspace(-2  , 2  , self.accuracy[1] - 1))
        idx2 = np.digitize(obs[2], np.linspace(-0.4, 0.4, self.accuracy[2] - 1))
        idx3 = np.digitize(obs[3], np.linspace(-3.5, 3.5, self.accuracy[3] - 1))
        return idx0, idx1, idx2, idx3

class solver:
    def __init__(self,env,  numEpisods, numTrys):
        self.env = env
        self.numEpisods = numEpisods
        self.maxTry = numTrys
        self.transformer =  transformer()
        self.lr = 0.001
        self.dr = 0.99

        self.Q = np.random.uniform(-1, 1, self.transformer.shape(self.env.action_space.n))

    def explorationTrheshold(self, e):
        min_th = 0.25
        max_th = 0.75
        return max_th - e / self.numEpisods * (max_th - min_th)

    def selectAction(self, obs, ep):
        epcilon = np.random.uniform()
        thr = self.explorationTrheshold(ep)

        if epcilon < thr:
            return env.action_space.sample()
        else:
            return np.argmax(self.Q[self.transformer.transform(obs)])

    def qValues(self, obs, act = -1):
        if act == -1:
            return self.Q[self.transformer.transform(obs)]
        else:
            return self.Q[self.transformer.transform(obs)][act]

    def learningRate(self, ep):
        return 0.05

    def updateQTable(self, crntObs, act, newObs, reward):
        G = reward + np.max(self.qValues(newObs))
        oldQ = self.qValues(crntObs, act)

        idx = self.transformer.transform(crntObs)
        self.Q[idx][act] = oldQ + self.lr * (self.dr * G - oldQ)

    def playOnEpisoc(self, ep):
        self.lr = self.learningRate(ep)
        crntObs = env.reset()
        counter = 0
        done = False
        while not done and counter < self.maxTry:
            counter += 1
            action = self.selectAction(crntObs, ep)
            newObs, reward, done, info = self.env.step(action) 

            if done and counter < self.maxTry:
                reward = -300

            self.updateQTable(crntObs, action, newObs,  reward)
            crntObs = newObs
        return counter

    def loadQTable(self, fileName):
        #"Q-Learning/Mountain-Car/Qtable_final.txt"
        self.Q = np.loadtxt(fileName).reshape(self.transformer.shape(-1))

    def learn(self, startEp = 0):
        rewards = []
        for ep in range(startEp, self.numEpisods):
            reward = self.playOnEpisoc(ep)
            rewards.append(reward)

            if (ep % 1000 == 0 and ep > 0):
                name = "Q-Learning/CartPole/Qtable_{}.txt".format(ep) 
                np.savetxt(name, self.Q.reshape(1, -1))

            if (ep % 100 == 0 and ep > 0):
                print(ep, np.average(rewards))
                rewards = []

        np.savetxt("Q-Learning/CartPole/Qtable_final.txt", self.Q.reshape(1, -1))

    def play(self, render = False):
        done = False
        obs = self.env.reset()
        counter = 0
        while not done:
            counter += 1
            act = np.argmax(self.Q[self.transformer.transform(obs)])
            obs, reward, done, info = env.step(act)
            if(render):
                env.render()
        return counter

env = gym.make("CartPole-v1")

solver = solver(env, 20000, 5000)
#solver.learn()

solver.loadQTable("Q-Learning/CartPole/Qtable_final.txt")

rewards = []
wins = 0
U50 = 0
for i in range(10):
    r = solver.play(True)
    rewards.append(r)

print (np.min(rewards), np.average(rewards), np.max(rewards))
print (wins, U50)
    
