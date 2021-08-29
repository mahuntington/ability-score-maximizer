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
ability_scores = {}

def check_scores(scores):
    total = 0
    for score in scores.values():
        total += score_to_points[score]
    if total == 27:
        return True
    else:
        return False

def set_score(ability_index):
    if ability_index > 5:
        if check_scores(ability_scores):
            print(ability_scores)
    else:
        for score in score_to_points:
            ability_scores[abilities[ability_index]] = score
            set_score(ability_index+1)

set_score(0)


# for score in score_to_points:
    # ability_scores[abilities[0]] = score
    # for score in score_to_points:
        # ability_scores[abilities[1]] = score
        # for score in score_to_points:
            # ability_scores[abilities[2]] = score
            # for score in score_to_points:
                # ability_scores[abilities[3]] = score
                # for score in score_to_points:
                    # ability_scores[abilities[4]] = score
                    # for score in score_to_points:
                        # ability_scores[abilities[5]] = score
                        # if check_scores(ability_scores):
                            # # True
                            # print(ability_scores)

# for score in score_to_points:
    # print(score)
