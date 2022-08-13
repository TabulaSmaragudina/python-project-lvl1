#!/usr/bin/env python3


def main():
    print('Welcome to the Brain Games!')
    from brain_games.scripts.cli import welcome_user
    return welcome_user()

if __name__ == '__main__':
    main()

