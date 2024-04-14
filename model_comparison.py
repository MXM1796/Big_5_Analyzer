from txtai.pipeline import LLM
from txtai.pipeline import Textractor
import torch

def metric_1():
    pass

def metric_2():
    pass

def metric_3():
    pass


# Create LLM
llm = LLM("google/flan-t5-large", torch_dtype=torch.float32)
# query = "Answer folowing question: 'I easily make friends.' Possible response options are: very inaccurate, Neither accurate nor inaccurate, very accurate. Use the following text as a basis: 'Open-mindedness is the key to understanding each other.'"
query = "Beantworte mir folgende Frage auf deutsch: 'Ich gewinne leicht Freunde'. Mögliche Antwortmöglichkeiten sind: sehr unzutreffend, Weder zutreffend noch unzutreffend, sehr zutreffend. Nutzte als Basis folgenden Text: 'Aufgeschlossenheit ist der Schlüssel zum Verständnis füreinander.'"
result = llm(query)
print("LLM Standalone Result:")
print("Query: ", query, result)

print(result)
# textractor = Textractor()
# text = textractor('../testfile.txt')
# # print(text)
