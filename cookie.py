from thinkbayes import Pmf


pmf = Pmf("The vanilla cookie came from Jar 1")
pmf.set('Jar 1', 1, 0.5)
pmf.set('Jar 2', 1, 0.5)

pmf.mult('Jar 1', 0.75)
pmf.mult('Jar 2', 0.5)

pmf.normalize()

pmf.table()

