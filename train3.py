from thinkbayes import Suite
import matplotlib.pyplot as plt


class Train3(Suite):

    def __init__(self, hyp, hypos, alpha=1.0):
        Suite.__init__(self, hyp, None)
        self.hypos = hypos
        for hypo in hypos:
            self.set(hypo, 1/len(hypos))

    def likelihood(self, hypo, data):
        if hypo < data:
            return 0.0

        return 1/hypo


priors = [range(1, 501), range(1, 1001), range(1, 2001)]


for prior in priors:
    print("With a prior of uniform distribution 1 - %d with 3 observations" % prior[-1])

    train = Train3("How many trains does a company have if we see a train number", prior)
    for observation in [60, 30, 90, 70, 100, 45, 78, 20, 59]:
        train.update(observation, "How many trains does a company have if we see a train number %d" % observation)
        print("For observation: {}, Posterior distribution mean is: {}".format(observation, train.mean()))

    print("The credible interval is ({} - {})".format(train.percentile(5), train.percentile(95)))
    print()


plt.show()

