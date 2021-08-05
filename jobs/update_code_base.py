import os

import logger


def do():
    logger.info("Running job: " + str(__file__).split("/")[-1])
    directory: str = os.getenv("HOME") + "/scripts/"
    os.chdir(directory)
    os.system("./run.sh | tee -a run.log &")
    quit()


if __name__ == "__main__":
    do()
