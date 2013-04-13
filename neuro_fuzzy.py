from __future__ import division
__author__ = 'arunprasathshankar'
import itertools
import operator


class NeuroFuzzySystem(object):
    def __init__(self):
        self.word_list = []
        self.cog_list = []
        self.bigram_list = []
        self.cog_list_bigrams = []
        self.trigram_list = []
        self.cog_list_trigrams = []
        self.fourgram_list = []
        self.cog_list_fourgrams = []
        self.fivegram_list = []
        self.cog_list_fivegrams = []

    def neuroFuzzyModelling(self, tf_idf_list, u1, u2, u3, tf_idf_bigram_list, b1, b2, b3, tf_idf_trigram_list, t1, t2, t3, tf_idf_fourgram_list, f1, tf_idf_fivegram_list, p1):
        out = open('out.txt', 'w')
        for item in u1:
            out.write(str(item[0]) + " " + str(item[1]) + '\n')
        out.close()
        
        u1 = {item[0]: item[1:] for item in u1}
        u2 = {item[0]: item[1:] for item in u2}
        u3 = {item[0]: item[1:] for item in u3}

        b1 = {item[0]: item[1:] for item in b1}
        b2 = {item[0]: item[1:] for item in b2}
        b3 = {item[0]: item[1:] for item in b3}

        t1 = {item[0]: item[1:] for item in t1}
        t2 = {item[0]: item[1:] for item in t2}
        t3 = {item[0]: item[1:] for item in t3}

        f1 = {item[0]: item[1:] for item in f1}

        p1 = {item[0]: item[1:] for item in p1}
     
        for word, tf_idf in tf_idf_list.iteritems():
            try:
                x, y = u1[word], u2[word]
                
            except KeyError:
                continue

            A = x[1] * x[2]
            B = x[3] * x[4]
            C = y[1] * y[2] + 1
            D = y[3] * y[4] + 1
            #E = z[2] * z[3] + 1
            #F = z[4] * z[5] + 1
            #mfs = [[A, B], [C, D], [E, F]]
            mfs = [[A, B], [C, D]]
            #weights = sum([x[3], x[5], y[3], y[5], z[3], z[5]])
            weights = sum([x[2], x[4], y[2], y[4]])
            rule_inputs = list(itertools.product(*mfs))
            len_comb = len(rule_inputs)
            # 6 --> write code to find this automatically
            #weight_factor = (len(mfs) * len_comb) / 6
            weight_factor = (len(mfs) * len_comb) / 4
            weights *= weight_factor
            rule_inputs = sum([sum(r) for r in rule_inputs])
            self.defuzzifyUnigrams(word, rule_inputs, weights)

        for bigram, tf_idf in tf_idf_bigram_list.iteritems():
            x = b1.get(bigram)
            if not x is None:
                A = x[1] * x[2]
                B = x[3] * x[4]
                mfs = [[A, B]]
                weights = sum([x[2], x[4]])
                rule_inputs = list(itertools.product(*mfs))
                len_comb = len(rule_inputs)
                # 6 --> write code to find this automatically
                weight_factor = (len(mfs) * len_comb) / 2
                weights *= weight_factor
                rule_inputs = sum([sum(r) for r in rule_inputs])
                self.defuzzifyBigrams(bigram, tf_idf, rule_inputs, weights)
        
        for trigram, tf_idf in tf_idf_trigram_list.iteritems():
            x = t1.get(trigram)
            if not x is None:
                A = x[1] * x[2]
                B = x[3] * x[4]
                mfs = [[A, B]]
                weights = sum([x[2], x[4]])
                rule_inputs = list(itertools.product(*mfs))
                len_comb = len(rule_inputs)
                # 6 --> write code to find this automatically
                weight_factor = (len(mfs) * len_comb) / 2
                weights *= weight_factor
                rule_inputs = sum([sum(r) for r in rule_inputs])
                self.defuzzifyTrigrams(trigram, tf_idf, rule_inputs, weights)

        for fourgram, tf_idf in tf_idf_fourgram_list.iteritems():
            x = f1.get(fourgram)
            if not x is None:
                A = x[1] * x[2]
                B = x[3] * x[4]
                mfs = [[A, B]]
                weights = sum([x[2], x[4]])
                rule_inputs = list(itertools.product(*mfs))
                len_comb = len(rule_inputs)
                # 6 --> write code to find this automatically
                weight_factor = (len(mfs) * len_comb) / 2
                weights *= weight_factor
                rule_inputs = sum([sum(r) for r in rule_inputs])
                self.defuzzifyFourgrams(fourgram, tf_idf, rule_inputs, weights)

        for fivegram, tf_idf in tf_idf_fivegram_list.iteritems():
            x = p1.get(fivegram)
            if not x is None:
                A = x[1] * x[2]
                B = x[3] * x[4]
                mfs = [[A, B]]
                weights = sum([x[2], x[4]])
                rule_inputs = list(itertools.product(*mfs))
                len_comb = len(rule_inputs)
                # 6 --> write code to find this automatically
                weight_factor = (len(mfs) * len_comb) / 2
                weights *= weight_factor
                rule_inputs = sum([sum(r) for r in rule_inputs])
                self.defuzzifyFivegrams(fivegram, tf_idf, rule_inputs, weights)

    def defuzzifyUnigrams(self, word, rule_inputs, weights):
        cog = rule_inputs / weights
        self.word_list.append(word)
        self.cog_list.append(cog)

    def defuzzifyBigrams(self, bigram, tf_idf, rule_inputs, weights):
        cog = rule_inputs / weights
        #print bigram, tf_idf, cog
        self.bigram_list.append(bigram)
        self.cog_list_bigrams.append(cog)

    def defuzzifyTrigrams(self, trigram, tf_idf, rule_inputs, weights):
        cog = rule_inputs / weights
        self.trigram_list.append(trigram)
        self.cog_list_trigrams.append(cog)

    def defuzzifyFourgrams(self, fourgram, tf_idf, rule_inputs, weights):
        cog = rule_inputs / weights
        self.fourgram_list.append(fourgram)
        self.cog_list_fourgrams.append(cog)

    def defuzzifyFivegrams(self, fivegram, tf_idf, rule_inputs, weights):
        cog = rule_inputs / weights
        self.fivegram_list.append(fivegram)
        self.cog_list_fivegrams.append(cog)

    def normCOGUnigrams(self):
        if not len(self.cog_list) == 0:
            self.max_cog = max(self.cog_list)
        self.cog_list = [cog / self.max_cog for cog in self.cog_list]
        word_rank = dict(zip(self.word_list,     self.cog_list))
        sorted_word_rank = sorted(word_rank.iteritems(), key=operator.itemgetter(1))
        for item in sorted_word_rank:
            print item[0], item[1]

    def normCOGBigrams(self):
        max_cog = max(self.cog_list_bigrams)
        self.cog_list_bigrams = [cog / max_cog for cog in self.cog_list_bigrams]
        word_rank = dict(zip(self.bigram_list, self.cog_list_bigrams))
        sorted_word_rank = sorted(word_rank.iteritems(), key=operator.itemgetter(1))
        print '*********** BIGRAMS ***********'
        for item in sorted_word_rank:
            print item[0], item[1]

    def normCOGTrigrams(self):
        max_cog = max(self.cog_list_trigrams)
        self.cog_list_trigrams = [cog / max_cog for cog in self.cog_list_trigrams]
        word_rank = dict(zip(self.trigram_list, self.cog_list_trigrams))
        sorted_word_rank = sorted(word_rank.iteritems(), key=operator.itemgetter(1))
        print '*********** TRIGRAMS ***********'
        for item in sorted_word_rank:
            print item[0], item[1]

    def normCOGFourgrams(self):
        max_cog = max(self.cog_list_fourgrams)
        self.cog_list_fourgrams = [cog / max_cog for cog in self.cog_list_fourgrams]
        word_rank = dict(zip(self.fourgram_list, self.cog_list_fourgrams))
        sorted_word_rank = sorted(word_rank.iteritems(), key=operator.itemgetter(1))
        print '*********** FOURGRAMS ***********'
        for item in sorted_word_rank:
            print item[0], item[1]

    def normCOGFivegrams(self):
        if not len(self.cog_list_fivegrams) == 0:
            max_cog = max(self.cog_list_fivegrams)
            self.cog_list_fivegrams = [cog / max_cog for cog in self.cog_list_fivegrams]
            word_rank = dict(zip(self.fivegram_list, self.cog_list_fivegrams))
            sorted_word_rank = sorted(word_rank.iteritems(), key=operator.itemgetter(1))
            print '*********** FIVEGRAMS ***********'
            for item in sorted_word_rank:
                print item[0], item[1]
        else:
            print '*********** FIVEGRAMS ***********'
            print None