import pycorpora
import random
import tracery
from tracery.modifiers import base_english

fruits = pycorpora.foods["fruits"]

rules = {
    'origin': '#greeting.capitalize#, #fruit#!',
    'greeting': ['hello', 'greetings', 'howdy', 'hey'],
    'fruit': random.sample(fruits["fruits"], 10),
    'location': ['world', 'solar system', 'galaxy', 'universe']
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print grammar.flatten("#origin#") # prints, e.g., "Hello, world!"


#print random.choice(fruits["fruits"])


