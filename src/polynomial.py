class Polynomial(object):

    def __init__(self, coefficients, variable):
        self.coefficients = coefficients
        self.variable = variable

    def __repr__(self):
        return 'Polynomial(%r, %r)' % (self.coefficients, self.variable)

    def __str__(self):
        """
        Convert list of coefficients into a user readable string.
        :return:
        """
        result = []
        for i in range(len(self.coefficients)-1, -1, -1):
            if self.coefficients[i]:
                if i < len(self.coefficients) - 1:
                    if self.coefficients[i] >= 0:
                        result.append('+')
                    else:
                        result.append('-')
                    result.append(self.__to_string_monomial(abs(self.coefficients[i]), i))
                else:
                    result.append(self.__to_string_monomial(self.coefficients[i], i))
        return ' '.join(result)

    def __to_string_monomial(self, coefficient, power):
        """
        Convert a monomial to string.
        :param coefficient: coefficient of monomial
        :param power: power of monomial
        :return: String in form coefficientx^power
        """
        if power == 1:
            if coefficient == 1:
                return 'x'
            elif coefficient == -1:
                return '-x'
            return '%sx' % coefficient
        elif power:
            if coefficient == 1:
                return 'x^%d' % power
            elif coefficient == -1:
                return '-x^%d' % power
            return '%sx^%d' % (coefficient, power)
        return "%s" % coefficient

    def __abs__(self):
        """
        Evaluate value of polynomial for a given value of variable.
        """
        result = 0
        if self.variable is None:
            return self.coefficients[0]
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * pow(self.variable, i)
        return result