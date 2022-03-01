
class Logger:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix
    
    def log(self, line) -> None:
        print(f'[{self.prefix}] {line}')