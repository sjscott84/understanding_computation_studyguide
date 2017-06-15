class Number:

    def __init__(self, value):
        self.number = value

    def __str__(self):
        return '{}'.format(self.number)

    def reducible(self):
        return False

    def get(self):
        return self.number


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '({} + {})'.format(self.left, self.right)

    def reducible(self):
        return True

    def reduce(self):
        if self.left.reducible():
            return Add(self.left.reduce(), self.right)
        elif self.right.reducible():
            return Add(self.left, self.right.reduce())
        else:
            return Number(self.left.get() + self.right.get())


class Multiply:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '({} * {})'.format(self.left, self.right)

    def reducible(self):
        return True

    def reduce(self):
        if self.left.reducible():
            return Multiply(self.left.reduce(), self.right)
        elif self.right.reducible():
            return Multiply(self.left, self.right.reduce())
        else:
            return Number(self.left.get() * self.right.get())

class Machine:
    def __init__(self, expression):
        self.expression = expression
        print self.expression
        self.run()

    def step(self):
        self.expression = self.expression.reduce()
        print self.expression

    def run(self):
        while self.expression.reducible():
            self.step()



calc = Machine(Add(Multiply(Number(1),Number(2)), 
               Multiply(Number(3),Number(4))))
number = Number(5)

#print calc
#print calc.reducible()
#calc = calc.reduce()
#print calc
#print calc.reducible()
#calc = calc.reduce()
#print calc
#print calc.reducible()
#calc = calc.reduce()
#print calc
#print calc.reducible()