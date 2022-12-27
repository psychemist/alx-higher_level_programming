#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = 0

    if a_dictionary is None or a_dictionary == {}:
        return None
    for name in a_dictionary.keys():
        for score in a_dictionary.values():
            if score > max_score:
                max_score = score
        if a_dictionary[name] == max_score:
            return name
