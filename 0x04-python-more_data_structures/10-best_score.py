#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return
    else:
        best_score = 0
        for score in a_dictionary.values():
            if best_score < score:
                best_score = score
        for name, score in a_dictionary.items():
            if score == best_score:
                return name
