import scores
import random


my_dict = {}

for key in range(50):
    my_dict[str(key)] = random.randint(1,5)

my_scores = scores.calculate_big5_scores(my_dict)

print(my_scores)


