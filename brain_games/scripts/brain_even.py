#!/usr/bin/env/python3
from brain_games.games import even_logic
from brain_games.logic.engine import run_game


def main():
    run_game(even_logic)


if __name__ == '__main__':
    main()
