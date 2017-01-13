class Polynomial(object):

    def __init__(self, coefficients, variable):
        self.coefficients = coefficients
        self.variable = variable

    def __repr__(self):
        return 'Polynomial(%r, %r)' % (self.coefficients, self.variable)
