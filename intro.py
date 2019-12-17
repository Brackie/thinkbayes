from thinkbayes import Pmf


pmf = Pmf()

for i in [1, 2, 3, 4, 5, 6]:
    pmf.set(i, 1/6.0)

pmf.table()
