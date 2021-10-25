from collections import defaultdict, OrderedDict
from csv import reader
from itertools import chain, combinations
from optparse import OptionParser
from fpgrowth_py.utils import *
from fpgrowth_py import fpgrowth


def fpgrowthFromFile(fname, minSupRatio, minConf):
    itemSetList, frequency = getFromFile(fname)

    freqItemSet, rules = fpgrowth(itemSetList, minSupRatio, minConf)
    print(rules)
    print("----------------------")
    print(freqItemSet)


if __name__ == "__main__":
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='inputFile',
                         help='CSV filename',
                         default=None)
    optparser.add_option('-s', '--minSupport',
                         dest='minSup',
                         help='Min support (float)',
                         default=0.5,
                         type='float')
    optparser.add_option('-c', '--minConfidence',
                         dest='minConf',
                         help='Min confidence (float)',
                         default=0.5,
                         type='float')


    (options, args) = optparser.parse_args()
  
    fpgrowthFromFile(options.inputFile, options.minSup, options.minConf)