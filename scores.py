import numpy as np

def score_extroversion(answer_scores):
    return 20 + answer_scores['0'] - answer_scores['5'] + answer_scores['10'] - answer_scores['15'] + answer_scores['20'] - answer_scores['25'] + answer_scores['30'] - answer_scores['35'] + answer_scores['40'] - answer_scores['45']

def score_agreeableness(answer_scores):
    return 14 - answer_scores['1'] + answer_scores['6'] - answer_scores['11'] + answer_scores['16'] - answer_scores['21'] + answer_scores['26'] - answer_scores['31'] + answer_scores['36'] - answer_scores['41'] + answer_scores['46']

def score_conscientiousness(answer_scores):
    return 14 + answer_scores['2'] - answer_scores['7'] + answer_scores['12'] - answer_scores['17'] + answer_scores['22'] - answer_scores['27'] + answer_scores['32'] - answer_scores['37'] + answer_scores['42'] - answer_scores['47']

def score_neuroticism(answer_scores):
    return 38 - answer_scores['3'] + answer_scores['8'] - answer_scores['13'] + answer_scores['18'] - answer_scores['23'] + answer_scores['28'] - answer_scores['33'] + answer_scores['38'] - answer_scores['43'] + answer_scores['48']

def score_openess(answer_scores):
    return 8 + answer_scores['4'] - answer_scores['9'] + answer_scores['14'] - answer_scores['19'] + answer_scores['24'] - answer_scores['29'] + answer_scores['34'] - answer_scores['39'] + answer_scores['44'] - answer_scores['49']


def calculate_big5_scores(answer_scores):
    scores = {
        'extroversion': score_extroversion(answer_scores), 
        'agreeableness': score_agreeableness(answer_scores), 
        'conscientiousness': score_conscientiousness(answer_scores), 
        'neuroticism': score_neuroticism(answer_scores), 
        'openess': score_openess(answer_scores)
        }
    
    return scores
