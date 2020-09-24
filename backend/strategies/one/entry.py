class StrategyMap:
    def __init__(self, context=None):
        self.context = context

    def action_a(self):
        print("I'm the action of first strategy!")
        return True

    def go(self):
        self.action_a()
        print("I'm the go method!")

