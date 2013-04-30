__author__ = 'arun'


from collections import defaultdict
import itertools
import networkx as nx


class ConceptSkeleton(object):
    def __init__(self, edges):
        self.edges = edges
        self.inference_paths = []
        self.concepts = {}

    def extractInferencePaths(self):
        #  amazing one-liner to extract concept skeletons
        g1 = nx.Graph(self.edges)
        self.skeletons = nx.connected_components(g1)[:]

        neighbors = {}
        for edge in self.edges:
            neighbors[edge[0]] = edge[1]

        for edge in self.edges:
            neighbor = neighbors.get(edge[1])
            if neighbor:
                self.inference_paths.append([edge[0], edge[1], neighbor])

        v = defaultdict(list)
        for key, value in sorted(neighbors.iteritems()):
            v[value].append(key)
        for key, value in v.iteritems():
            if not len(list(itertools.combinations(value, 2))) == 0:
                for item in list(itertools.combinations(value, 2)):
                    self.inference_paths.append([item[0], key, item[1]])
        print
        print '******* Inference paths *******'
        for path in self.inference_paths:
            print path

    def extractConcepts(self):
        print
        print '******* Skeletons *******'
        for skeleton in self.skeletons:
            print skeleton
        print
        print '******* Concepts *******'

        for skeleton in self.skeletons:
            concept_paths = []
            for path in self.inference_paths:
                for node in path:
                    if node in skeleton:
                        concept_paths.append(path)
                        break
            self.concepts[tuple(skeleton)] = concept_paths
        print
        for skeleton, inference_paths in self.concepts.iteritems():
            print skeleton, inference_paths






