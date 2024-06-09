import numpy as np

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
