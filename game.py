import pycorpora
import random
import tracery
from tracery.modifiers import base_english

# configuarion
number_of_rooms = 2

objects = random.sample(pycorpora.objects['objects']['objects'], number_of_rooms)
#print pycorpora.objects['objects']['objects']
rooms = random.sample(pycorpora.architecture.rooms['rooms'], number_of_rooms)
room_names = []
for i in range(0,number_of_rooms):
    room_names.append( "%s %s" % (objects[i], rooms[i]) )

# generate room names
def generateRoomNames():
    room_name_rules = {
        'origin': '#objects# #rooms#',
        'objects': objects,
        'rooms': rooms
    }
    grammar = tracery.Grammar(room_name_rules)
    grammar.add_modifiers(base_english)
    room_names = {}
    for i in range(0,number_of_rooms):
        room_names[i] = grammar.flatten("#origin#")
    return room_names
#room_names = generateRoomNames()
#print room_names


def printRoom(index):
    fruits = pycorpora.foods["fruits"]
    rules = {
        'origin': '#name_of_room.capitalizeAll# is a room. The description of #name_of_room# is "#fruit.s.capitalize# are here!"\n',
        'name_of_room': room_names[index],
        #'room_items': random.sample(pycorpora.get_file(category, subcategory)[subcategory], 10),
        'fruit': random.sample(fruits["fruits"], 10),
        'location': ['world', 'solar system', 'galaxy', 'universe']
    }
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    print grammar.flatten("#origin#") # prints, e.g., "Hello, world!"


def printHeader():
    print '"A Randomized Inform Game" by Martin Grider\n'


printHeader()
for i in range(0,number_of_rooms):
    printRoom( i )

