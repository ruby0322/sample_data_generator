from config import Config
import datetime
import os

class Writer:
    def __init__(self, config: Config) -> None:
        self.out_put_folder_path: str = config.output_folder_path
        self.file_path: str = ''

    def create_file(self, output_folder_path: str) -> bool:
        if (self.file_path): return False
        self.file_path = f'{os.getcwd()}/{output_folder_path}/{datetime.datetime.now().strftime("%H%M%S%m%d%Y")}.txt'
        with open(self.file_path, 'w') as f:
            return True

    def write_line(self, line) -> bool:
        if not self.file_path:
            return False
        with open(self.file_path, 'a') as f:
            f.write(line)
            f.write('\n')
        return True

    def get_file_path(self) -> str:
        return self.file_path
            