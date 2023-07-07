import yaml


def load_story(filename):
    with open(filename) as file:
        content = yaml.safe_load(file)
        return Story(content)


class Choice:
    @property
    def text(self):
        return self.data["choice"]

    @property
    def next(self):
        return self.data["next"]

    @property
    def response(self):
        return self.data["response"] if 'response' in self.data.keys() else None

    @property
    def items(self):
        return self.data["items"] if 'items' in self.data.keys() else []

    @property
    def hooks(self):
        return self.data["hooks"] if 'hooks' in self.data.keys() else []

    @property
    def fight_results(self):
        action = self.data["next"]
        if type(action) is not dict:
            return False

        results = action if any(s in action.keys() for s in ('win', 'loss')) else None
        return (results["win"], results["loss"]) if results else False

    def __init__(self, data):
        self.data = data


class Action:
    @property
    def name(self):
        return self.data["name"]

    @property
    def description(self):
        return self.data["desc"]

    def __init__(self, data):
        self.data = data
        self.choices = []
        for choice in self.data["choices"]:
            self.choices.append(Choice(choice))

    def get_choice(self, idx):
        return self.choices[idx]


class Story:

    @property
    def title(self):
        return self.data["game"]["title"]

    @property
    def prologue(self):
        return self.data["game"]["prologue"]

    @property
    def start(self):
        return self.data["game"]["start"]

    def __init__(self, data):
        self.data = data

    def get_action(self, id):
        actions = self.data['game']['actions']
        for action in actions:
            if action['action'] == id:
                return Action(action)

        return None
