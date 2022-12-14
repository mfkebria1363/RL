import gym
# create and initialize the environment
env = gym.make("CartPole-v1")
print(env.observation_space)
print(env.action_space)
print(env.observation_space.low)
print(env.observation_space.high)


env.reset()

print ( 10**env.observation_space.shape[0])

# play 10 games

l = 0
h = 0

for i in range(1000):
    # initialize the variables
    done = False
    game_rew = 0
    while not done:
        # choose a random action
        action = env.action_space.sample()
        env.render()
        # take a step in the environment
        new_obs, rew, done, info = env.step(action)
        l = min(l, new_obs[0])
        h = max(l, new_obs[0])
        game_rew += rew
        # print (new_obs)
        # # when is done, print the cumulative reward of the game and reset the environment
        if done:
            print('Episode %d finished, reward:%d' % (i, game_rew))
            env.reset()
            print (l, h)