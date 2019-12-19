from thinkbayes import Suite
import matplotlib.pyplot as plt


class Train(Suite):

    def likelihood(self, hypo, data):
        if hypo < data:
            return 0.0

        return 1/hypo


priors = [range(1, 501), range(1, 1001), range(1, 2001)]

for color, prior in zip(["r-", "g-", "b-"], priors):
    print("With a prior of uniform distribution 1 - %d" % prior[-1])

    train = Train("How many trains does a company have if we see a train number 60", prior)
    train.update(60)

    print("The posterior distribution mean is %.3f" % train.mean())
    print("")

    plt.plot(train.hypotheses(), train.probs(), color)

# When we use more observations, the mean of the posterior distributions begin to converge
print("When we use more observations, the mean of the posterior distributions begin to converge")

for prior in priors:
    print("With a prior of uniform distribution 1 - %d with 3 observations" % prior[-1])

    train = Train("How many trains does a company have if we see a train number", prior)
    for observation in [60, 30, 90]:
        train.update(observation, "How many trains does a company have if we see a train number %d" % observation)
        print("For observation: {}, Posterior distribution mean is: {}".format(observation, train.mean()))

    print("")

plt.show()

