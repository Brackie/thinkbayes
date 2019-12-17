from thinkbayes import Pmf


pmf = Pmf("The yellow M n M came from the 1994 bag")

# A is the probability bag 1 is from 1994 and bag 2 is from 1996
# B is the probability bag 1 is from 1996 and bag 2 is from 1994

# Setting the priors
pmf.set("A", 1, 1/2)
pmf.set("B", 1, 1/2)

# Our data says the probability of the yellow is 20% and green 20% for H(A)
# And the probability of the yellow is 14% and green 20% for H(B)
# Finding the posterior based on priors and likelihoods
pmf.mult("A", 20 * 20)
pmf.mult("B", 14 * 10)

# Normalizing the data using Bayes theorem
pmf.normalize()

# Displaying the data
pmf.table()
