import gymnasium as gym
import numpy as np
from gymnasium import spaces
from yahtzee import Yahtzee

class SingleAgentEnv(gym.Env):
    # rendering will simply be printing the sheet as a table, and printing the dice?
    metadata = {"render_modes": ["human"]}

    def __init__(self) -> None:
        self.yahtzee = Yahtzee()

        self.observation_space = spaces.Dict(
            {
                "sheet": spaces.Box(
                    low=np.array([-1]*13),
                    high=np.array([5, 10, 15, 20, 25, 30, 30, 30, 25, 30, 40, 1250, 30]),
                    dtype=np.int16
                ),
                "bonus": spaces.Discrete(2),
                "dice": spaces.Box(
                    low=np.array([1]*5),
                    high=np.array([6]*5),
                    dtype=np.int8
                ),
                "reamining_rolls": spaces.Discrete(3)
            }
        )

        # self.action_space = ... TODO