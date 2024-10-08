# Big_5_Analyzer
Analyzing texts and generate big 5 scores trough answers of txtai LLM

**General idea of how to proceed (31.08.2024):** 
Since, we are no experts in psychology or computer science, we should shift the focus from backend to 
the front end and expand functions and design. After a first good blueprint, we can 
start looking for money or experts to improve backend. 

## To Do

- Write a how to start document  
- implement further functional ideas to frontend
- make front end usable for "people"
- improve front end design

[//]: # (- find about five models than can be used with Python &#40;done&#41;)

[//]: # (- make a sample of questions &#40;done&#41;)

[//]: # (- test the models)

[//]: # (- make a benchmark test with the models )

[//]: # (- Kontexte und Antworten generieren &#40;done&#41;)

[//]: # (- Metriken ausdenken, um die Performance von den Modellen zu vergleichen)

[//]: # (- look for unambigous videos and define scores)

[//]: # (- clean code + comment)


## Brainstorming_score_accuracy_improvement and measurement
- exclude ambivalent scores (both scores are small or high)
- weighting of sentences - non linear layer (implement softmax function)
- test different and more keywords
- scattering?
- runtime of single response
- runtime of several responses
- response precision 
- response accuracy 
- score selection depending on videos




## Models to test
source: https://huggingface.co/models?pipeline_tag=question-answering&sort=downloads

1. https://huggingface.co/deepset/roberta-base-squad2 (done & works)
2. https://huggingface.co/mrm8488/longformer-base-4096-finetuned-squadv2 (transfered)
3. https://huggingface.co/timpal0l/mdeberta-v3-base-squad2 (transfered)
4. https://huggingface.co/google-bert/bert-large-uncased-whole-word-masking-finetuned-squad
5. https://huggingface.co/distilbert/distilbert-base-cased-distilled-squad (transfered)

## Important Sources


Scoring Sheet: https://sites.temple.edu/rtassessment/files/2018/10/Table_BFPT.pdf

    1. Extraversion
    2. Agreeableness
    3. Conscientiousness
    4. Neuroticism
    5. Openness to Experience

Tutorial: Build Your First Question Answering System 
https://haystack.deepset.ai/tutorials/01_basic_qa_pipeline