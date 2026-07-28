from transformers import pipeline

# Load sentiment analysis model
classifier = pipeline("sentiment-analysis")

# Test it
result = classifier(["I love building AI applications with FastAPI",
    "This is terrible, I hate everything about it",
    "The weather is okay today"])
print(result)