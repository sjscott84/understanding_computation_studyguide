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

    def reduce(self, environment):
        if self.left.reducible():
            return Add(self.left.reduce(environment), self.right)
        elif self.right.reducible():
            return Add(self.left, self.right.reduce(environment))
        else:
            return Number(self.left.get() + self.right.get())


class Subtract:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '({} - {})'.format(self.left, self.right)

    def reducible(self):
        return True

    def reduce(self, environment):
        if self.left.reducible():
            return Subtract(self.left.reduce(environment), self.right)
        elif self.right.reducible():
            return Subtract(self.left, self.right.reduce(environment))
        else:
            return Number(self.left.get() - self.right.get())


class Multiply:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '({} * {})'.format(self.left, self.right)

    def reducible(self):
        return True

    def reduce(self, environment):
        if self.left.reducible():
            return Multiply(self.left.reduce(environment), self.right)
        elif self.right.reducible():
            return Multiply(self.left, self.right.reduce(environment))
        else:
            return Number(self.left.get() * self.right.get())


class Divide:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '({} / {})'.format(self.left, self.right)

    def reducible(self):
        return True

    def reduce(self, environment):
        if self.left.reducible():
            return Divide(self.left.reduce(environment), self.right)
        elif self.right.reducible():
            return Divide(self.left, self.right.reduce(environment))
        else:
            return Number(self.left.get() / self.right.get())


class Variable:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{}'.format(self.name)

    def reducible(self):
        return True

    def reduce(self, environment):
        return environment[self.name]



class Machine:
    def __init__(self, expression, environment):
        self.expression = expression
        self.environment = environment
        print self.expression
        self.run()

    def step(self):
        self.expression = self.expression.reduce(self.environment)
        print self.expression

    def run(self):
        while self.expression.reducible():
            self.step()

#test = Machine(Variable('x'), {'x': Number(4)})
#test = Machine(Add(Variable('x'), Variable('y')),
#               {'x': Number(4), 'y': Number(10)})

test2 = Machine(Add(Multiply(Variable('x'), Number(5)),
                 Divide(Variable('y'), Number(2))),
                 {'x': Number(5), 'y': Number(10)})

#calc = Machine(Subtract(Divide(Number(12),Number(2)), 
#               Multiply(Number(3),Number(4))))
#number = Number(5)

#x = Variable('x')
#print x

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