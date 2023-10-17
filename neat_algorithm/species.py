class Species:
    def __init__(self, mem):
        self.members = []
        self.members.append(mem)
        self.rep = self.members[0]
        self.threshold = 3
        pass

    def add(self, brain):
        self.members.append(brain)
        # TODO: Check fitness and set as rep
        if self.rep.fitness < brain.fitness:
            self.rep = self.members[-1]

    def check(self, brain):
        cd = self.rep.calculate_compatibility(brain)
        return cd < self.threshold

    def get_len(self):
        return len(self.members)

    def evaluate(self):
        print('Evaluating Species')
        pass
