import os


def do():
    home_directory: str = os.getenv("HOME")
    update_script: str = "/scripts/update.sh"
    os.system("./" + home_directory + update_script)


if __name__ == "__main__":
    do()
