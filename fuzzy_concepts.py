__author__ = 'arun'
import pygraphviz as pgv


class FuzzyConcept(object):
    def __init__(self, f1, f1_2):
        self.f1 = f1
        self.f1_2 = f1_2

    def normalizeProximityScores(self):
        ps = []
        pi = []
        self.header = self.f1.next()
        for row in self.f1:
            pi.append(float(row[1]))
            ps.append(float(row[2]))
        self.max_ps = max(ps)
        self.min_pi = min(pi)
        self.max_pi = max(pi)
        self.denum = self.max_pi - self.min_pi

    def writeFinalPISheet(self, f2):
        f2.writerow(self.header)
        self.f1_2.next()
        for row in self.f1_2:
            f2.writerow(
                [row[0], (float(row[1]) - self.min_pi) / self.denum, float(row[2]) / self.max_ps, row[3], row[4],
                 row[5]])

    def drawConceptGraphs(self, f, graph):
        f.next()
        for row in f:
            #print row[0], row[2], row[3]
            graph.add_node(row[0], color='goldenrod2', style='filled', shape='box', xlabel=round(float(row[1]), 2))
            graph.add_node(row[3], color='goldenrod2', style='filled', shape='box', xlabel='0000')
            graph.add_edge(row[0], row[3], color='sienna', style='filled', label=round(float(row[2]), 2))
        graph.write('graph.dot')
        img = pgv.AGraph(file='graph.dot')  # img = pgv.AGraph('graph.dot') doesn't work | bug in Pygraphviz
        img.layout(prog='dot')
        img.draw('concepts.pdf')
        img.close()