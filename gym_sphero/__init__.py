# -*- coding: utf-8 -*-

"""Top-level package for OpenAI Gym for Sphero Robots."""

__author__ = """Leigh Johnson"""
__email__ = 'leigh@data-literate.com'
__version__ = '0.0.1'
from gym.envs.registration import register

register(
    id='sphero-v0',
    entry_point='gym_sphero.envs:SpheroEnv',
)