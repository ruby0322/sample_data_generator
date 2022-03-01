if __name__ == '__main__':
    from config import Config
    from generator import Generator
    from writer import Writer
    from logger import Logger
    import random
    import os

    config = Config(f'{os.getcwd()}/config.json')
    generator = Generator(config)
    writer = Writer(config)
    logger = Logger('System')

    logger.log('Creating file...')
    writer.create_file(config.output_folder_path)
    logger.log(f'File created. New file be found at {writer.get_file_path()}')

    logger.log(f'Generating sample data...')
    if config.multiple_delimiters:
        for i in range(config.line_cnt):
            line: str = ''
            nums: list[str] = [generator.generate() for _ in range(config.number_cnt_per_line)]
            is_first: bool = True
            for num in nums:
                if not is_first: line += random.choice(config.delimiters)
                else: is_first = False
                line += num
            writer.write_line(line)
    else:
        for i in range(config.line_cnt):
            writer.write_line(config.delimiter.join(list(map(str, [generator.generate() for _ in range(config.number_cnt_per_line)]))))
    logger.log(f'Sample data generated successfully. Enjoy!')
