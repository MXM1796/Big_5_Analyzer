# Testing model tinyroberta-squad2

# tinyroberta-squad2

# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
#
# model_name = "deepset/tinyroberta-squad2"
#
# # ("Beantworte mir folgende Frage auf deutsch: 'Ich gewinne leicht Freunde'. "
# #  "Mögliche Antwortmöglichkeiten sind: sehr unzutreffend, "
# #  "Weder zutreffend noch unzutreffend, sehr zutreffend. Nutzte als Basis folgenden Text: "
# #  "'Aufgeschlossenheit ist der Schlüssel zum Verständnis füreinander.'")
#
# # a) Get predictions
# nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
# # QA_input = {
# #     'question': "Do you agree regarding: I Am the life of the party ",
# #     'context': "I 'm not a fan of large crowds and loud music. I prefer spending time with a few close friends and relaxing in a quieter environment."
# # }
# # res = nlp(QA_input)
#
#
# # a) Get predictions
# # nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
# QA_input = {
#     'question': 'Why is model conversion important?',
#     'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
# }
# res = nlp(QA_input)
#
#
# print(res)



from transformers import AutoTokenizer, AlbertForMultipleChoice
import torch

tokenizer = AutoTokenizer.from_pretrained("albert/albert-base-v2")
model = AlbertForMultipleChoice.from_pretrained("albert/albert-base-v2")

prompt = "Statement: I Am the life of the party; Context: I love being at parties and feeling the energy of the people around me. I'm usually the one cracking jokes, cranking up the music, and getting people to dance. I would definitely say I'm the life of the party."
choice0 = "I agree."
choice1 = "I disagree"
labels = torch.tensor(0).unsqueeze(0)  # choice0 is correct (according to Wikipedia ;)), batch size 1

encoding = tokenizer([prompt, prompt], [choice0, choice1], return_tensors="pt", padding=True)
outputs = model(**{k: v.unsqueeze(0) for k, v in encoding.items()}, labels=labels)  # batch size is 1

print(outputs)
# the linear classifier still needs to be trained
# loss = outputs.loss
# logits = outputs.logits
# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

