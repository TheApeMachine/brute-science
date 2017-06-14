# BRUTE-SCIENCE
#
# Brute-force a scoring algorithm for matching resources to keywords.

import re
import random
from itertools import repeat
from resource import Resource

def main():
    keywords   = ['food']
    expansions = ['food', 'eat', 'restaurant']
    resources  = Resource().small_test

    kl0 = 0.0
    kl1 = 0.0

    fl1 = 0.0
    fl2 = 0.0
    fl3 = 0.0
    fl4 = 0.0
    fl5 = 0.0

    eureka     = False
    iterations = 0
    samples    = len(resources)

    while eureka is False:
        results     = {'positive': 0, 'neutral': 0, 'negative': 0}
        iterations += 1

        for k in keywords:
            for r in resources:
                score = 0.0

                if r["category"] == k:
                    score += kl0 + fl1
                if r['matchers'].count(k):
                    score += kl0 + fl2
                if r['title'].count(k):
                    score += kl0 + fl3
                if r['desc'].count(k):
                    score += kl0 + fl4
                if r['tags'].count(k):
                    score += kl0 + fl5

                r['score'] += score

        for k in expansions:
            for r in resources:
                score = 0.0

                if r["category"] == k:
                    score += kl1 + fl1
                if r['matchers'].count(k):
                    score += kl1 + fl2
                if r['title'].count(k):
                    score += kl1 + fl3
                if r['desc'].count(k):
                    score += kl1 + fl4
                if r['tags'].count(k):
                    score += kl1 + fl5

                r['score'] += score

        sorted_resources = sorted(resources, key=lambda k: k['score'])

        c1 = 0
        c2 = 1
        c3 = 2

        result_count = 0

        for i in xrange((len(sorted_resources) / 3)):
            results['negative'] += sorted_resources[c1]['status']
            results['neutral']  += sorted_resources[c2]['status']
            results['positive'] += sorted_resources[c3]['status']

            c1 += (samples / 3) + 1
            c2 += (samples / 3) + 1
            c3 += (samples / 3) + 1

            result_count += 1

        # print 'NEGATIVE: {}'.format(results['negative'])
        # print 'NEUTRAL : {}'.format(results['neutral'])
        # print 'POSITIVE: {}'.format(results['positive'])

        if results['positive'] is result_count and results['neutral'] is 0 and results['negative'] is -result_count:
            # We have found the optimal weights.
            eureka = True
        else:
            # Reset the scores.
            for r in resources:
                r['score'] = 0.0

            # Adjust the weights.
            kl0 = random.uniform(0.1, 1.0)
            kl1 = random.uniform(0.1, 1.0)
            fl1 = random.uniform(0.1, 1.0)
            fl2 = random.uniform(0.1, 1.0)
            fl3 = random.uniform(0.1, 1.0)
            fl4 = random.uniform(0.1, 1.0)
            fl5 = random.uniform(0.1, 1.0)

    print 'ITERATIONS      : {}'.format(iterations)
    print 'KEYWORD LEVEL 1 : {}'.format(kl0)
    print 'KEYWORD LEVEL 2 : {}'.format(kl1)
    print 'CATEGORY        : {}'.format(fl1)
    print 'MATCHERS        : {}'.format(fl2)
    print 'TITLE           : {}'.format(fl3)
    print 'DESCRIPTION     : {}'.format(fl4)
    print 'TAGS            : {}'.format(fl5)


if __name__ == "__main__":
    main()
