from sMail import *
from sMail.config import log_path


def clear_log():
    if input("Are you sure you want to delete the log?(Y/n)").upper() == "Y":
        clear(log_path)
    else:
        pass


def main():
    print("BEGIN...")
    send()
    print("OVER...")


if __name__ == "__main__":
    main()
