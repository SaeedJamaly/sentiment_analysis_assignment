import nltk
from nltk import FeatureEarleyChartParser, load_parser

# The grammar
grammar = load_parser('grammar.fcfg', trace=0, parser=FeatureEarleyChartParser)

# The sentence to be parsed
sent = 'your sentence '

# Tokenizing the sentence
tokens = sent.split()

# Create the parse tree
trees = grammar.parse(tokens)

# parsed sentence and the visual output of parse tree
for tree in trees: 
    print(tree)
    print(tree.label())
    print(tree.label()['SNTMNT'])
    tree.draw()