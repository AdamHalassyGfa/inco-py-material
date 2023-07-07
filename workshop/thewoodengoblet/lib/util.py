import textwrap
import re


def print_text(text):
    txt = textwrap.wrap(text, width=80)
    for line in txt:
        print(line)
    print()


def validate_input(key):
    pattern = re.compile('^\s*([0-9]+||[qQiI])\s*$')
    return pattern.match(key)


def input_choice(game, action):
    while True:
        idx = 0
        while idx < len(action.choices):
            choice = action.choices[idx]
            idx += 1
            print(f'  {idx}) {choice.text}')

        print("  ---")
        print('  I) View inventory')
        print('  Q) Quit game')

        key = input("\nWhat do you do? ")
        if not validate_input(key):
            print("\n** This is impossible!\n")
            continue

        if key == 'q' or key == 'Q':
            return None

        if key == 'i' or key == 'I':
            return -2

        choice = int(key) - 1
        if choice < 0 or choice > len(action.choices):
            print("** This is impossible!\n")
            continue

        return action.get_choice(choice)
