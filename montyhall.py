from thinkbayes import Pmf


pmf = Pmf("After contestant chooses door A, Monty opens door B and their is no car")

# Setting the priors

pmf.set('Door 1', 1, 1/3)
pmf.set('Door 2', 1, 1/3)
pmf.set('Door 3', 1, 1/3)

# Finding probabilities based on the priors and likelihoods
pmf.mult("Door 1", 1/2)
pmf.mult('Door 2', 0)
pmf.mult('Door 3', 1)

# Normalizing the data using Bayes theorem
pmf.normalize()

# Displaying the data
pmf.table()


