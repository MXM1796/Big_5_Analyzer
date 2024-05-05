import pandas as pd


def benchmark_questions(question_amount_from_top):

    df = pd.read_csv("big_five_statements.txt", sep=",", usecols=[0])

    question = [row[0] for col, row in df.iterrows()]

    return question[:question_amount_from_top]

print(benchmark_questions(20))



