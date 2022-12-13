import gym
import time

# create the environment
env = gym.make('Tennis-ramDeterministic-v3')
# reset the environment before starting
env.reset()
# loop 10 times
done = False
for i in range(50):
    # take a random action
    if(not done):
        state, reward, done, data=env.step(env.action_space.sample())
        # render the game
        env.render()

# close the environment
env.close()