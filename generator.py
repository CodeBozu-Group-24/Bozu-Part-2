import openai

def gpt3Classification(query, examples, labels):
    a=openai.Classification.create(
        search_model="ada",
        model="curie",
        examples=examples,
        query=query,
        labels=labels,
    )
    return a