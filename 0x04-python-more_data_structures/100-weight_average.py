#!/usr/bin/python3
def weight_average(my_list=[]):
    score, weight = 0, 0
    for (scores, weights) in my_list:
        score += scores * weights
        weight += weights
    return score / weight
