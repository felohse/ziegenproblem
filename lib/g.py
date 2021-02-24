import random
from lib.candidate import Candidate
from lib.gate import Gate

class Game:

    def __init__(self):
        if random.randrange(2) == 0:
            self.candidate = Candidate('stay')
        else:
            self.candidate = Candidate('switch')
        self.gates = [Gate() for i in range(3)]
        random.choice(self.gates).has_ziege = True

    def result(self):
        self.candidate.choose_gate(self.gates)
        for gate in self.gates:
            if gate != self.candidate.choosen_gate and not gate.has_ziege:
                self.gates.remove(gate)
        self.candidate.choose_again(self.gates)
        return (self.candidate.tactic, self.candidate.choosen_gate.has_ziege)