from thinkbayes import Pmf


pmf = Pmf("Elvis was an identical twin")

# Setting priors on all
pmf.set("A", 1, 0.08)
pmf.set("B", 1, 0.92)

# Finding probabilities based on the priors and likelihoods
pmf.mult("A", 1)
pmf.mult("B", 1/2)

# Normalizing the data using Bayes theorem
pmf.normalize()

# Display the posteriors
pmf.table()
