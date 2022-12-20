from __future__ import annotations

import numpy as np
from ConfigSpace import Configuration, ConfigurationSpace, Float
from src.datasets.dataset import Dataset
from src.models.model import Model


class Branin(Model):
    def __init__(self, dataset: Dataset | None = None) -> None:
        super().__init__(dataset)

    @property
    def configspace(self) -> ConfigurationSpace:
        # Build Configuration Space which defines all parameters and their ranges
        cs = ConfigurationSpace(seed=0)

        # First we create our hyperparameters
        x1 = Float("x1", (-5, 10), default=0)
        x2 = Float("x2", (0, 15), default=0)

        # Add hyperparameters and conditions to our configspace
        cs.add_hyperparameters([x1, x2])

        return cs

    def train(self, config: Configuration, seed: int) -> float:
        x1 = config["x1"]
        x2 = config["x2"]
        a = 1.0
        b = 5.1 / (4.0 * np.pi**2)
        c = 5.0 / np.pi
        r = 6.0
        s = 10.0
        t = 1.0 / (8.0 * np.pi)
        
        return a * (x2 - b * x1**2 + c * x1 - r) ** 2 + s * (1 - t) * np.cos(x1) + s

