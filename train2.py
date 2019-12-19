from thinkbayes import Suite
import matplotlib.pyplot as plt


class Train2(Suite):

    def __init__(self, hyp, hypos, alpha=1.0):
        Suite.__init__(self, hyp, None)
        self.hypos = hypos
        for hypo in hypos:
            self.set(hypo, hypo ** (-alpha))
        self.normalize()

    def likelihood(self, hypo, data):
        if hypo < data:
            return 0.0

        return 1/hypo


priors = [range(1, 501), range(1, 1001), range(1, 2001)]

# When we use the power law of distribution where the number of companies in a
# certain tier is  inversely proportional to the number of locomotives each owns,
#  the mean of the posterior distributions begin to converge

print('''When we use the power law of distribution where the number of companies in a 
certain tier is  inversely proportional to the number of locomotives each owns,the mean 
of the posterior distributions begin to converge\n''')

for prior in priors:
    print("With a prior of uniform distribution 1 - %d with 3 observations" % prior[-1])

    train = Train2("How many trains does a company have if we see a train number", prior)
    for observation in [60, 30, 90]:
        train.update(observation, "How many trains does a company have if we see a train number %d" % observation)
        print("For observation: {}, Posterior distribution mean is: {}".format(observation, train.mean()))

    print("The credible interval is ({} - {})".format(train.percentile(5), train.percentile(95)))
    print()


plt.show()

