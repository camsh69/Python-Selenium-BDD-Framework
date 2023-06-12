import os
import logging
import time


class Logger:
    def __init__(self, logger, file_level=logging.INFO, log_directory="./logs"):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter(
            "%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s"
        )

        curr_time = time.strftime("%Y-%m-%d")
        log_file_name = f"log{curr_time}.txt"
        log_file_path = os.path.join(log_directory, log_file_name)

        # "a" to append the logs in the same file, "w" to generate new logs and delete the old one
        fh = logging.FileHandler(log_file_path, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
