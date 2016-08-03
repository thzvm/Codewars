class Plugboard(object):

    def __init__(self, wires):
        '''wires: This is the mapping of pairs of characters'''

        self.wires = {}

        if wires:
            if len(wires) > 26:
                raise ValueError('error message')

            for wire in [wires[i: i + 2] for i in range(0, len(wires), 2)]:
                if wire[0] in self.wires or wire[1] in self.wires:
                    raise ValueError('error message')
                self.wires[wire[0]] = wire[1]
                self.wires[wire[1]] = wire[0]
        else:
            return

    def process(self, c):
        '''c: The single character to process'''
        if c in self.wires:
            return self.wires[c]
        else:
            return c

if __name__ == '__main__':

    plugboard = Plugboard("AB")
    print(plugboard.process('A'))
