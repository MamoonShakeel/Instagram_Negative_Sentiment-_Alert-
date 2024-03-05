from transformers import pipeline

def get_sentiment(text):
    """
    Implements sentiment analysis on text
    output will be a list of dictionaries containing 
    labels and scores
    """
    distilled_student_sentiment_classifier = pipeline(
        model = 'mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis',
        # return_all_scores=True
    )

    output = distilled_student_sentiment_classifier(text)
    # print(output)
    
    return output[0]['label']


