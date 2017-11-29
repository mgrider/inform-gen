import pycorpora
import random
import tracery
import containers
from tracery.modifiers import base_english

# configuarion
map_height = 2
map_width = 2
number_of_rooms = map_height * map_width

objects = random.sample(pycorpora.objects['objects']['objects'], number_of_rooms)
#print pycorpora.objects['objects']['objects']
old_room_names = random.sample(pycorpora.architecture.rooms['rooms'], number_of_rooms)
settings = random.sample(pycorpora.archetypes.setting['settings'], number_of_rooms)
fruits = random.sample(pycorpora.foods.fruits['fruits'], number_of_rooms)
colors = random.sample(pycorpora.colors.xkcd['colors'], number_of_rooms)
container_list = random.sample(containers.containers, number_of_rooms)
#print container_list

room_names = []
item_names = []
container_items = []
for i in range(0,number_of_rooms):
    room_names.append( "%s %s" % (objects[i], settings[i]['name']) )
    item_names.append( "%s %s" % (colors[i]['color'], objects[i]) )
    container_items.append( "%s %s" % (settings[i]['name'], container_list[i]) )
    
#print container_items

item_names_copy = list(item_names)
random.shuffle(item_names_copy)

def printRules(rules):
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    print grammar.flatten("#origin#") # prints, e.g., "Hello, world!"


def printHeader():
    print '\n\n"A Procedurally Generated Inform Game" by Martin Grider\n'
    print 'Include Exit Lister by Gavin Lambert.'
    print "Use scoring. The maximum score is %i." % (number_of_rooms)

def printFooter():
    print '\nEvery turn:\n\tif the score is the maximum score: \n\t\tsay "you won!"; \n\t\tend the story.'


printHeader()

for y in range(0,map_height):
    for x in range(0,map_width):
        room_name_index = (y * map_width) + x
#        understand_and = '" and "'
#        understand_words = room_names[room_name_index].split()
#        understand_string = 'Understand "' + understand_and.join(understand_words) + '" as ' + room_names[room_name_index] + '.\n'
        rules = {
            'origin': '#[roomSynonym:#room_synonyms#]origin_after_actions#',
            'origin_after_actions': '\n#name_of_room.capitalizeAll# is a room. The description of #name_of_room# is "#description#".\n#understand_string##scenery##fruit_string#\n#item_string#\n#item_container_string#',
            'understand_string': '',#understand_string,
            'name_of_room': room_names[room_name_index],
            #'room_items': random.sample(pycorpora.get_file(category, subcategory)[subcategory], 10),
            'fruit': fruits[room_name_index],
            'fruit_descriptor': ['tantilizing','lonely-looking','moldy','sweet','half-eaten','disgusting','delicious','juicy'],
            'fruit_description': ['That is some #fruit_descriptor# looking #fruit#!','The #fruit# looks #fruit_descriptor#.', 'There are several #fruit_descriptor# #fruit.s# in the #room_basic#.'],
            'fruit_initial_text': ['There is #fruit.a# here.', 'Curiously, there is #fruit.a# here.'],
            'fruit_string': ['\n#fruit.a.capitalize# is in #name_of_room#. The #fruit# is edible. "#fruit_initial_text#" The description of #fruit# is "#fruit_description#"'],
            # item_names
            'item_name': item_names_copy[room_name_index],
            'item_color': colors[room_name_index]['color'],
            'matching_item_name': item_names[room_name_index],
            'item_container_name': container_items[room_name_index],
            'item_description_initial': ['There is #item_name.a# here.'],
            'item_description_examined': ['The #item_name# looks like it could fit inside something...', 'The only thing special about #item_name# is that it is really #item_color#.', 'That #item_name# is really quite #item_color#.'],
            'item_placed_success': ['You really put that in its place!'],
            'item_container_description_initial': ['There is #item_container_name.a.capitalize# here.'],
            'item_container_description_examined': ['That is some #item_container_name#!','The #item_container_name# looks it could fit something in it.', 'The #item_container_name# looks like it has room for something inside.'],
            'item_string': '#item_name.a.capitalizeAll# is in #name_of_room.capitalizeAll#. "#item_description_initial#" The description of #item_name.capitalizeAll# is "#item_description_examined#"',
            'item_container_string': '#item_container_name.a.capitalizeAll# is a container in #name_of_room.capitalizeAll#. #item_container_name.capitalizeAll# is closed and openable. "#item_container_description_initial#" The description of #item_container_name.capitalizeAll# is "#item_container_description_examined#"\nEvery turn:\n\tif the #matching_item_name.capitalizeAll# is in #item_container_name.capitalizeAll#:\n\t\tincrease the score by 1;\n\t\tnow the #matching_item_name.capitalizeAll# is nowhere;\n\t\tsay "#item_placed_success#".',
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
            rule = {
                'origin': '#room_name.capitalizeAll# is west of #east_room_name.capitalizeAll#.',
                'room_name': room_names[room_name_index],
                'east_room_name': room_names[east_index]
            }
            printRules(rule)
            #print '%s is west of %s.' % (room_names[room_name_index], room_names[east_index])
        if (y < map_height - 1):
            south_index = ((y+1) * map_width) + x
            rule = {
                'origin': '#room_name.capitalizeAll# is north of #south_room_name.capitalizeAll#.',
                'room_name': room_names[room_name_index],
                'south_room_name': room_names[south_index]
            }
            printRules(rule)
            #print '%s is north of %s.\n' % (room_names[room_name_index], room_names[south_index])


printFooter()

print '\n\n'
