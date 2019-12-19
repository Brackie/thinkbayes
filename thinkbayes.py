from numpy import array


class Pmf:
    """
    Class to represent a distribution of Mutually Exclusive and
    Collectively comprehensive variables with total probability
    H - Hypotheses
    D - Data
    Prior P(H) - is the initial probability of an hypotheses without seeing the data
    Likelihood P(D|H) - is the probability of an event happening given the hypotheses
    Posterior P(H|D) - is the probability of the hypotheses given the data
    Posterior = ((Prior * Likelihood) / Normalizing Constant)
    Normalizing constant P(D) - is the probability of an event happening under any hypotheses
    """

    def __init__(self, hyp):
        self.hyp = hyp
        self.variables = list()
        self.probabilities = list()

    def set(self, x, p):
        """Function to assign prior P(H) probabilities to the different hypotheses"""
        if x in self.variables:
            raise ValueError("Value already exists")

        self.variables.append(x)
        self.probabilities.append(p)

    def mult(self, x, p):
        """Function to assign multiply probabilities by a certain value usually likelihoods P(D|H)"""
        if x not in self.variables:
            raise ValueError("Value doesn't exists")

        i = self.variables.index(x)
        self.probabilities[i] *= p

    def prob(self, x):
        """Function to return probability of a hypotheses x"""
        if x not in self.variables:
            raise ValueError("Value doesn't exists")

        i = self.variables.index(x)
        return self.probabilities[i]

    def hypotheses(self):
        return array(self.variables)

    def probs(self):
        return array(self.probabilities)

    def normalize(self, fraction=1.0):
        """Function to normalize the probabilities by dividing through by the normalizing constant"""
        total = self.cumulative()
        if total == 0.0:
            raise ValueError("Probability is 0")

        factor = float(fraction) / total
        for i in range(len(self.variables)):
            self.probabilities[i] *= factor

    def cumulative(self):
        return sum(self.probabilities)

    def table(self):
        """Utility function to print results"""
        print("H: " + self.hyp)
        for i in range(len(self.variables)):
            print("X: {}, p(x): {}".format(self.variables[i], self.probabilities[i]))


class Cdf:

    def __init__(self):
        self.hyp = list()
        self.cp = list()

    def make(self, hypos, probs):
        total = 0.0
        for hypo, prob in zip(hypos, probs):
            total += prob
            self.hyp.append(hypo)
            self.cp.append(total)

    def percentile(self, hypo):
        i = self.hyp.index(hypo)
        return self.cp[i]


class Suite(Pmf):

    """Template class extends Pmf"""
    def __init__(self, hyp, hypos=None):
        Pmf.__init__(self, hyp)

        if hypos is None:
            hypos = list()
        self.hypos = hypos

        self.n = len(hypos)
        for hypo in hypos:
            self.set(hypo, 1/self.n)

    def update(self, data, hyp=None):
        """Updates the probabilities of the hypothesis based on data and likelihood"""
        if hyp is not None:
            self.hyp = hyp

        for hypo in self.hypos:
            like = self.likelihood(hypo, data)
            self.mult(hypo, like)
        self.normalize()

    def likelihood(self, hypo, data):
        """returns likelihood of a specific hypothesis"""

    def mean(self):
        """Function to find the mean of the posterior distribution"""
        total = 0
        for hypo, prob in zip(self.hypotheses(), self.probs()):
            if not str(hypo).isdigit():
                raise TypeError("Value is not a digit")

            total += hypo * prob
        return total

    def percentile(self, percent):
        """Function to get the value at the 'percent' percentile"""
        total = 0.0
        p = percent / 100.0
        for hypo, prob in zip(self.hypotheses(), self.probs()):
            total += prob
            if total >= p:
                return hypo











