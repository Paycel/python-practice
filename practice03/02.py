class C32:
    def __init__(self):
        self.state = 'A'

    def flip(self):
        if self.state == 'A':
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'F':
            self.state = 'G'
            return 7
        elif self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise RuntimeError

    def coast(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'G':
            self.state = 'D'
            return 10
        elif self.state == 'H':
            self.state = 'D'
            return 11
        else:
            raise RuntimeError

    def daub(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise RuntimeError
