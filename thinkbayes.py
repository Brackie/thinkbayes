class Pmf:

    def __init__(self, hyp):
        self.hyp = hyp
        self.variables = list()
        self.frequencies = list()
        self.probabilities = list()

    def set(self, x, f, p):
        if x in self.variables:
            raise ValueError("Value already exists")

        self.variables.append(x)
        self.frequencies.append(f)
        self.probabilities.append(p)

    def mult(self, x, p):
        if x not in self.variables:
            raise ValueError("Value doesn't exists")

        i = self.variables.index(x)
        self.probabilities[i] *= p

    def prob(self, x):
        if x not in self.variables:
            raise ValueError("Value doesn't exists")

        i = self.variables.index(x)
        return self.probabilities[i]

    def normalize(self, fraction=1.0):
        total = self.cumulative()
        if total == 0.0:
            raise ValueError("Probability is 0")

        factor = float(fraction) / total
        for i in range(len(self.variables)):
            self.probabilities[i] *= factor

    def cumulative(self):
        return sum(self.probabilities)

    def table(self):
        print("H: " + self.hyp)
        for i in range(len(self.variables)):
            print("X: {}, f(x): {}, p(x): {}".format(self.variables[i], self.frequencies[i], self.probabilities[i]))
