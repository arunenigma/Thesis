from itertools import groupby
import csv


class SectionWiseClustering(object):
    def __init__(self, PI_bundle_unigrams, section_bundle):
        self.PI_bundle_unigrams = PI_bundle_unigrams
        self.section_bundle = section_bundle
        self.section_headers = {}
        self.section_headers_ranges = []

    # Scheme 2 - Scheme with heading and normal rags
    def key(self, item):
        return [int(x) for x in item[1].split()[:3]]

    def findSectionHeaders(self):
        if not len(self.section_bundle) < 1:

            for k, v in groupby(self.section_bundle, key=self.key):
                self.section_headers[' '.join(str(x) for x in k)] = [' '.join(x[0] for x in v)]

            self.section_headers_range_pivots = {}

            for ind, section in self.section_headers.iteritems():
                self.section_headers_range_pivots[int(ind.split(' ')[2])] = section[0]

            for ind, section in sorted(self.section_headers_range_pivots.items()):
                self.section_headers_ranges.append([ind, section])
        else:
            self.noSectionUnigramsPISheet()

    def clusterWordsBySection(self):
        if not len(self.section_bundle) < 1:  # check condition for no section docs eg. softjin
            c = csv.writer(open('pi_sheet.csv', 'wb'))
            c.writerow(['Word', 'PI Score', 'Tf-Idf', 'Loc Ind', 'Loc Sig', 'Section'])
            for i, sect in enumerate(self.section_headers_ranges):
                if not (i + 1) > len(self.section_headers_ranges) - 1:
                    #print sect[1]
                    for word, info in self.PI_bundle_unigrams.iteritems():
                        if sect[0] <= int(info[1][1].split(' ')[2]) < self.section_headers_ranges[i + 1][0]:
                            print word, info[0]
                            c.writerow([word, info[0], info[1][0], info[1][1], info[1][2], sect[1]])
                    print

            print self.section_headers_ranges[-1][1]
            for word, info in self.PI_bundle_unigrams.iteritems():
                if int(info[1][1].split(' ')[2]) > self.section_headers_ranges[-1][0]:
                    print word, info[0]
                    c.writerow([word, info[0], info[1][0], info[1][1], info[1][2], self.section_headers_ranges[-1][1]])

    def noSectionUnigramsPISheet(self):
        c = csv.writer(open('pi_sheet_softjin.csv', 'wb'))
        c.writerow(['Word', 'PI Score', 'Tf-Idf', 'Loc Ind', 'Loc Sig', 'Section'])
        for word, info in self.PI_bundle_unigrams.iteritems():
            c.writerow([word, info[0], info[1][0], info[1][1], info[1][2], 'NA'])