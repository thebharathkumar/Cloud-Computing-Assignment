import requests
import json


endpoint = ""
subscription_key = ""


api_url = endpoint + "/text/analytics/v3.1-preview.3/sentiment"


headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key
}


data = {
    "documents": [
        {
            "language": "en",
            "id": "1",
            "text": "I love this product! It's amazing!"
        },
        {
            "language": "en",
            "id": "2",
            "text": "This movie is terrible. I hate it!"
        }
    ]
}


response = requests.post(api_url, headers=headers, json=data)
result = response.json()


if response.status_code == 200:
   
    sentiments = result['documents']

   
    for sentiment in sentiments:
        sentiment_score = sentiment['confidenceScores']['positive']
        sentiment_label = "Positive" if sentiment_score >= 0.5 else "Negative"
        print("Document ID:", sentiment['id'])
        print("Sentiment:", sentiment_label)
        print("Score:", sentiment_score)
        print()
else:
    print("Error:", response.status_code, response.reason)
