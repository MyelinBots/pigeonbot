import random


class Action:
    def __init__(self, action: str, items: list, format: str, actionPoint: int):
        self.action = action
        self.items = items
        self.format = format
        self.actionPoint = actionPoint

    def actionPoint(self):
        return self.actionPoint

    def action(self):
        return self.action

    def items(self):
        return self.items

    def format(self):
        return self.format

    def act(self, name: str):
        # choose random item
        item = random.choice(self.items)

        return self.format % (name, self.action, item)

