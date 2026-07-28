# tranformer is a library of hugging face
pipeline is tool which is ready-made ai assembly line

python
from transformers import pipeline

You're importing a tool called pipeline from HuggingFace's transformers library. Think of pipeline as a ready-made AI assembly line — you just tell it what job to do and it handles everything internally.

python
classifier = pipeline("sentiment-analysis")

You're creating an AI worker called classifier. You told it its job is sentiment analysis — reading text and deciding if it's positive or negative. HuggingFace downloads a pre-trained model automatically. You didn't train anything. Someone else trained it on millions of sentences — you're just using it.

python
result = classifier("I love building AI applications with FastAPI")

You're giving your AI worker a sentence to analyze. It reads it and returns its judgment. Like asking a person "does this sentence sound happy or sad?"

python
print(result)

Print what the AI decided.

Expected output will look like:

python
[{"label": "POSITIVE", "score": 0.9998}]

label → what the AI decided (POSITIVE or NEGATIVE)
score → how confident it is (0 to 1, closer to 1 = very confident)