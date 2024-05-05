# Big_5_Analyzer
Analyzing texts and generate big 5 scores trough answers of txtai LLM


## ToDo
- find about five models than can be used with Python (done)
- make a sample of questions (done)
- test the models
- make a benchmark test with the models 
- Kontexte und Antworten generieren (done)
- Metriken ausdenken, um die Performance von den Modellen zu vergleichen


## Metriken
- response precision 
- response accuracy 
- speed of single response
- speed of several responses



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