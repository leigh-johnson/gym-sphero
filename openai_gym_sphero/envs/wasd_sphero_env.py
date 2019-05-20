# python
import logging
# lib
import gym
from gym import error, spaces, utils
from gym.utils import seeding

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class SpheroEnv(gym.Env):
    metadata = {'render.modes': ['human', 'ansi']}

    def __init__(self):
        pass

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass

    def close(self):
        pass
