'''
Main entry point into internal logic.
'''

import sys
import argparse
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    '''
    Parsing of input arguments.
    '''
    p = argparse.ArgumentParser()

    command_choices = ['show-example', 'show-folder']

    p.add_argument('command', help='Command to run',
                   choices=command_choices, type=str)

    args = p.parse_args()
    return args


def get_execution_file() -> str:
    '''
    Returns the absolute path of the current execution file.
    '''
    return Path(__file__).absolute().as_posix()


def custom_main():
    '''
    Main entry point to your code.
    '''
    args = parse_arguments()
    print()
    print(sys.version)
    print('Current Folder:', Path().absolute())

    if args.command == 'show-example':
        print('Just running an example')

    if args.command == 'show-folder':
        print('Execution File:', get_execution_file())


if __name__ == '__main__':
    custom_main()
