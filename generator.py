from config import Config
import random

class Generator:
    NUMBER_TYPE_INT = 0
    NUMBER_TYPE_FLOAT = 1
    def __init__(self, config: Config) -> None:
        self.upper_bound = config.upper_bound
        self.lower_bound = config.lower_bound
        self.number_type: int = config.number_type
        self.number_step: int | float = config.number_step
        self.decimal_cnt: int = config.decimal_cnt

    def generate(self) -> str:
        if (self.number_type == Generator.NUMBER_TYPE_INT):
            return f'{random.choice(list(range(self.lower_bound, self.upper_bound, self.number_step)))}'
        elif (self.number_type == Generator.NUMBER_TYPE_FLOAT):
            import numpy as np
            return f'{random.choice(list(np.arange(self.lower_bound, self.upper_bound, self.number_step))):.{self.decimal_cnt}f}'
