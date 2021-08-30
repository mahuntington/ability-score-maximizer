import sys

isCSV = False
score_to_points = {
        15:9,
        14:7,
        13:5,
        12:4,
        11:3,
        10:2,
        9:1,
        8:0
        }
abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

def check_scores(scores):
    total = 0
    for score in scores.values():
        total += score_to_points[score]
    if total == 27:
        return True
    else:
        return False

def generates_scores(ability_index,ability_scores, possibilities):
    if ability_index > 5:
        if check_scores(ability_scores):
            possibilities.append(ability_scores.copy())
    else:
        for score in score_to_points:
            ability_scores[abilities[ability_index]] = score
            generates_scores(ability_index+1, ability_scores, possibilities)
    return possibilities

def print_possibilities(possibilities, isCSV):
    for possibility in possibilities:
        object_string = ''
        for ability in abilities:
            if isCSV:
                object_string += str(possibility[ability]) + ', '
            else:
                object_string += ability + ': ' + str(possibility[ability]) + ', '
        print(object_string)

def determine_modifier(score):
    return int((score - 10) / 2)

def generate_ordered_scores_obj():
    obj = {}
    for i in range(0,19):
        obj[i] = []
    return obj

def order_possiblities(possibilities):
    ordered_possibilities = generate_ordered_scores_obj()
    for possibility in possibilities:
        total_modifiers = 0
        for score in possibility:
            total_modifiers += determine_modifier(possibility[score])
        ordered_possibilities[total_modifiers].append(possibility)
    return ordered_possibilities

def modify_possibilities():
    for possibility in possibilities:
        for score_name in possibility:
            possibility[score_name] += racial_modifiers[score_name]

racial_modifiers = {}
sys.argv.pop(0)
for ability_index in range(0, len(abilities)):
    racial_modifiers[abilities[ability_index]] = int(sys.argv[ability_index])

possibilities = generates_scores(0, {}, [])
modify_possibilities()

ordered_possibilities = order_possiblities(possibilities)

for i in range(0,19):
    if ordered_possibilities[i]:
        if not isCSV:
            print('=================')
            print('')
            print(i)
            print('')
            print('=================')
        print_possibilities(ordered_possibilities[i], isCSV)
