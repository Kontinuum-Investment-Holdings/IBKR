import os


def do():
    home_directory: str = os.getenv("HOME")
    update_script: str = "/scripts/run.sh"
    os.system("." + home_directory + update_script)
    quit()


if __name__ == "__main__":
    do()
