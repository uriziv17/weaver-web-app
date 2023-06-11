import sys
import time
import os


def main():
    # sys.stdout.flush()
    word = sys.argv[1]
    print("start!!!")
    path = os.getcwd()
    print(path)
    print(os.listdir("./"))


if __name__ == "__main__":
    main()
