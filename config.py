import json

class Config:
    def __init__(self, config_path: str) -> None:
        with open(config_path, 'r') as f:
            for key, value in json.load(f).items():
                setattr(self, key, value)