# Testing model tinyroberta-squad2

# tinyroberta-squad2

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/tinyroberta-squad2"

# ("Beantworte mir folgende Frage auf deutsch: 'Ich gewinne leicht Freunde'. "
#  "Mögliche Antwortmöglichkeiten sind: sehr unzutreffend, "
#  "Weder zutreffend noch unzutreffend, sehr zutreffend. Nutzte als Basis folgenden Text: "
#  "'Aufgeschlossenheit ist der Schlüssel zum Verständnis füreinander.'")

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
# QA_input = {
#     'question': "Do you agree regarding: I Am the life of the party ",
#     'context': "I 'm not a fan of large crowds and loud music. I prefer spending time with a few close friends and relaxing in a quieter environment."
# }
# res = nlp(QA_input)


# a) Get predictions
# nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)


print(res)
# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

