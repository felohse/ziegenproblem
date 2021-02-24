import random


class Candidate:

    def __init__(self, tactic):
        self.tactic = tactic
        self.choosen_gate = None

    def choose_gate(self, list_gates):
        c_gate = random.choice(list_gates)
        self.choosen_gate = c_gate
        return c_gate

    def choose_again(self, list_gates):
        if self.tactic == 'stay':
            return self.choosen_gate
        elif self.tactic == 'switch':
            for gate in list_gates:
                if gate != self.choosen_gate:
                    self.choosen_gate = gate
                    return gate
        else:
            return None