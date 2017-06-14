class Number:

    def __init__(self, value):
        self.number = value

    def __str__(self):
        return '{}'.format(self.number)


class Add:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '({} + {})'.format(self.left, self.right)


class Multiple:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '({} * {})'.format(self.left, self.right)


calc = Add(Multiple(Number(1),Number(2)), 
           Multiple(Number(3),Number(4)))
number = Number(5)
print calc
print number