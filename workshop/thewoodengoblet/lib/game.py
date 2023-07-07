from lib import util
import random


class Game:

    def __init__(self, story):
        self.story = story
        self.items = []
        self.reputation = 0
        self.strength = 0


    def is_choice_available(self, choice):
        if not choice.when:
            return True

    def is_reputation_positive(self):
        return self.reputation > 0

    def add_item(self, item):
        if item not in self.items:
            print(f'You put the {item} into your backpack.')
            self.items.append(item)
        else:
            print(f'You already have this item.')

    def handle_dialog(self, choice):
        if choice.response:
            util.print_text(choice.response)

    def decrease_reputation(self):
        self.reputation -= 1
        print(f"Your reputation decreased to {self.reputation}.")

    def increase_reputation(self):
        self.reputation += 1
        print(f"Your reputation increased to {self.reputation}.")

    def increase_strength(self):
        self.strength += 1
        print(f"Your reputation increased to {self.reputation}.")

    def handle_items(self, choice):
        for item in choice.items:
            self.add_item(item)

    def handle_hooks(self, choice):
        for hook in choice.hooks:
            method = getattr(self, hook)
            method()

    def handle_fight(self, choice):
        fight = choice.fight_results
        if not fight:
            return None

        (win, loss) = fight
        outcome = random.randint(1, 6) + self.strength
        if outcome > 3:
            print("You won the fight, lucky man!")
            return win
        else:
            print("You lost the fight, and barely escaped.")
            return loss

    def handle_choice(self, choice):
        if not choice:
            return None

        # 1: Handle items:
        self.handle_items(choice)

        # 2: Handle hooks:
        self.handle_hooks(choice)

        # 2: Handle dialog:
        self.handle_dialog(choice)

        # 3: Handle fight:
        fight_outcome = self.handle_fight(choice)
        return fight_outcome if fight_outcome else choice.next

    def print_inventory(self):
        if len(self.items) == 0:
            print("Your backpack is empty.")
            return

        print("You have the following items:")
        for item in self.items:
            print(f'  - {item}')
        print('')

    def action(self, id):
        action = self.story.get_action(id)
        if not action:
            return None

        print(f'\nAt the "{action.name}"\n')
        util.print_text(action.description)
        choice = util.input_choice(action)
        if choice == -2:
            self.print_inventory()
            return id

        response = self.handle_choice(choice)

        return id if response == -2 else response

    def play(self):
        next_action = self.prologue()
        while next_action:
            next_action = self.action(next_action)

    def prologue(self):
        print(f'\n\n\n{self.story.title}\n')
        util.print_text(self.story.prologue)
        input("\nPress enter to begin your journey...")
        return self.story.start
