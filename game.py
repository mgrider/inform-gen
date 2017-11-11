import pycorpora
import random
import tracery
from tracery.modifiers import base_english

# configuarion
map_height = 3
map_width = 3
number_of_rooms = map_height * map_width

objects = random.sample(pycorpora.objects['objects']['objects'], number_of_rooms)
#print pycorpora.objects['objects']['objects']
old_room_names = random.sample(pycorpora.architecture.rooms['rooms'], number_of_rooms)
settings = random.sample(pycorpora.archetypes.setting['settings'], number_of_rooms)
fruits = random.sample(pycorpora.foods.fruits['fruits'], number_of_rooms)
room_names = []
for i in range(0,number_of_rooms):
    room_names.append( "%s %s" % (objects[i], settings[i]['name']) )


def printRules(rules):
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    print grammar.flatten("#origin#") # prints, e.g., "Hello, world!"


def printHeader():
    print '\n\n"A Randomized Inform Game" by Martin Grider\n'
    print 'Include Exit Lister by Gavin Lambert.\n'


printHeader()

for y in range(0,map_height):
    for x in range(0,map_width):
        room_name_index = (y * map_width) + x
#        understand_and = '" and "'
#        understand_words = room_names[room_name_index].split()
#        understand_string = 'Understand "' + understand_and.join(understand_words) + '" as ' + room_names[room_name_index] + '.\n'
        rules = {
            'origin': '#[roomSynonym:#room_synonyms#]origin_after_actions#',
            'origin_after_actions': '#name_of_room.capitalizeAll# is a room. The description of #name_of_room# is "#description#".\n#understand_string##scenery##fruit_string#',
            'understand_string': '',#understand_string,
            'name_of_room': room_names[room_name_index],
            #'room_items': random.sample(pycorpora.get_file(category, subcategory)[subcategory], 10),
            'fruit': fruits[room_name_index],
            'fruit_descriptor': ['tantilizing','lonely-looking','moldy','sweet','half-eaten','disgusting','delicious','juicy'],
            'fruit_description': ['That is some #fruit_descriptor# looking #fruit#!','The #fruit# looks #fruit_descriptor#.', 'There are several #fruit_descriptor# #fruit.s# in the #room_basic#.'],
            'fruit_initial_text': ['There is #fruit.a# here.', 'Curiously, there is #fruit.a# here.'],
            'fruit_string': ['', '\n#fruit.a.capitalize# is in #name_of_room#. The #fruit# is edible. "#fruit_initial_text#"'],
            #'scenery': '#fruit.capitalizeAll# is scenery in the #name_of_room.capitalizeAll#. The description of #fruit.capitalizeAll# is "#fruit_description#".',
            'room_synonyms': settings[room_name_index]['synonyms'],
            'room_qualities': settings[room_name_index]['qualities'],
            'room_basic': settings[room_name_index]['name'],
            'room_modifier': ['might once have been','could almost be', 'is almost certainly','is very likely', 'might someday be'],
            'description': 'This #room_qualities# #room_basic# #room_modifier# #roomSynonym.a#.',
            'scenery_description': ['Obviously, the #room_basic# isn\'t really #roomSynonym.a#.', 'The #room_basic# may look like #roomSynonym.a#, but you see that it\'s not.', 'No, #roomSynonym.a# isn\'t right.'],
            'scenery': '#roomSynonym.capitalizeAll# is scenery in the #name_of_room.capitalizeAll#. The description of #roomSynonym.capitalizeAll# is "#scenery_description#".',
            'location': ['world', 'solar system', 'galaxy', 'universe']
        }
        printRules(rules)
        # only need to do east and south
        if (x < map_width - 1):
            east_index = room_name_index + 1
            print '%s is west of %s.' % (room_names[room_name_index], room_names[east_index])
        if (y < map_height - 1):
            south_index = ((y+1) * map_width) + x
            print '%s is north of %s.\n' % (room_names[room_name_index], room_names[south_index])

print '\n\n'
