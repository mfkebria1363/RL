import gym
# create and initialize the environment
env = gym.make("CartPole-v1")
print(env.observation_space)
print(env.action_space)
print(env.observation_space.low)
print(env.observation_space.high)


env.reset()
# play 10 games
for i in range(3):
    # initialize the variables
    done = False
    game_rew = 0
    while not done:
        # choose a random action
        action = env.action_space.sample()
        env.render()
        # take a step in the environment
        new_obs, rew, done, info = env.step(action)
        game_rew += rew
        # when is done, print the cumulative reward of the game and reset the environment
        if done:
            print('Episode %d finished, reward:%d' % (i, game_rew))
            env.reset()