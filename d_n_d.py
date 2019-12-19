from thinkbayes import Suite


class DND(Suite):

    def likelihood(self, hypo, data):
        if hypo < data:
            return 0.0

        return 1/hypo


hypos = [4, 6, 8, 12, 20]

dnd = DND("What is the probability of picking a particular die if we roll a six", hypos)
dnd.update(6)

dnd.table()

for roll in [7, 7, 8, 9, 12, 8]:
    dnd.update(roll, hyp="What is the probability of picking a particular die if we roll a %s" % roll)
    dnd.table()
