#!/usr/bin/env/python
from pprint import pprint


class VectorSpaceModel(object):
    def __init__(self, specs):
        """
            An algebraic model for representing technical specifications as vectors of identifiers
            A document is represented as a vector. Each dimension of the vector corresponds to a
            separate term. If a term occurs in the document, then the value in the vector is non-zero.
        """
        self.specs = specs
        self.spec_vectors = []
        self.vector_indices = []
        if len(specs) > 0:
            self.buildVSM(specs)

    def buildVSM(self, specs):
        """
            Create vector space for passed document strings
        :param specs: passed documents
        """
        self.vector_indices = self.getVectorIndex(specs)
        self.spec_vectors = [self.createVectors(spec) for spec in specs]

    def getVectorIndex(self, specs):
        pass

    def createVectors(self, spec):
        pass

    def search(self, search_query_list):
        pass


if __name__ == '__main__':
    #test specs
    specs = ['the product is IEEE 754 compliant', 'floating point read write add/subtract barrel shifter',
             'amber ARM not compliant with IEEE 754', 'product supports USB and contains FPU']
    vsm = VectorSpaceModel(specs)
    pprint(vsm.search(['IEEE compliant']))