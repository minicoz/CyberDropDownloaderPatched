from cyberdrop_dl.main import main as main_dl
import sys


if __name__ == '__main__':
    print("""
    WAIT! If you're just trying to download files, check the README.md file for instructions.
    This file is intended for development usage ONLY.
    """)
    if input("Keep going? (y/N) ") == "y":
        sys.argv = ['--disable-attempt-limit']
        main_dl()
