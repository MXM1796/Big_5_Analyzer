# Import required modules and libraries
import pathlib
import networkx as nx
from txtai.embeddings import Embeddings
from txtai.graph import GraphFactory
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


# Initialize txtai Embeddings with a pre-configured model
embeddings = Embeddings({
    'path': "sentence-transformers/all-MiniLM-L6-v2"
})

# Load test data from a CSV file
test_csv = pd.read_csv('test2.csv', header=0, index_col=False, usecols=[1])

# Reset the DataFrame index
test_csv.reset_index(inplace=True)

# Extract the 'text' column from the DataFrame
data = test_csv["text"]

# Prepare data for txtai indexing
txtai_data = [(count, sent, None) for count, sent in enumerate(data)]

# Index data with txtai
embeddings.index(txtai_data)

def score_collector(word_arr):
    """
    Calculate the score for a word list.

    Parameters:
    - word_arr: List of words.
    - score: Threshold score.

    Returns:
    Score for the word list.
    """

    score_dict = {}
    for word in word_arr:
        res = embeddings.search(word, len(data))
        score_arr = np.array([item[1] for item in res])
        score_dict[word] = np.mean(score_arr)

    return score_dict
def read_keywords_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    keywords_dict = {}
    current_key = None

    for line in lines:
        line = line.strip()
        if line.endswith(':'):
            current_key = line[:-1]
            keywords_dict[current_key] = []
        elif current_key:
            keywords_dict[current_key].extend(line.split(', '))

    return {key: np.array(value) for key, value in keywords_dict.items()}

# Reading keywords from the file
file_path = 'keywords.txt'
keywords = read_keywords_from_file(file_path)
print(keywords)

big_5_characteristics = ["openness", "extraversion", "neuroticism","consciousness", "agreeableness"]

def score_low_high(characteristic, dict1, function):
    score_100_word = f"{characteristic}_100"
    score_0_word = f"{characteristic}_0"

    score_100 = function(dict1[score_100_word])
    score_0 = function(dict1[score_0_word])

    return score_100, score_0

a, b = score_low_high(big_5_characteristics[0], keywords, score_collector)

print(list(a.values()))


def score_calculation(score_100: dict, score_0: dict):
    mean_100 = np.mean(list(score_100.values()))
    mean_0 = np.mean(list(score_0.values()))

    return mean_100, mean_0

def final_score(a, b):
    return (a-b+1)/2

print(score_calculation(a, b))

print(final_score(*score_calculation(a, b)))






