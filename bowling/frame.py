class Frame:

    def __init__(self, number, initial=None):
        self.number = number
        self.rolls = []
        if initial:
            self.add_roll(initial)
        self.child = None

    def simple_score(self):
        return sum(self.rolls)

    def add_child(self, init):
        self.child = Frame(self.number + 1, init)

    def add_roll(self, roll):
        if self.complete() and self.child:
            self.child.add_roll(roll)
        elif self.complete():
            self.add_child(roll)
        else:
            self.rolls.append(roll)

    def complete(self):
        return self.strike() or self.full()

    def strike(self):
        try:
            return self.rolls[0] == 10
        except IndexError:
            return False

    def spare(self):
        return sum(self.rolls) == 10
    
    def full(self):
        return len(self.rolls) == 2
