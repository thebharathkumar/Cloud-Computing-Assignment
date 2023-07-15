import requests
import json


endpoint = ""
subscription_key = ""


image_url = ""

api_url = endpoint + "/vision/v3.0/analyze"


headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key
}


params = {
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en'
}


data = {
    'url': image_url
}


response = requests.post(api_url, headers=headers, params=params, json=data)
result = response.json()

if response.status_code == 200:
    # Image analysis results
    categories = result['categories']
    description = result['description']['captions'][0]['text']
    dominant_color = result['color']['dominantColorBackground']

    # Print the results
    print("Categories:")
    for category in categories:
        print(category['name'])
    
    print("\nDescription:", description)
    print("\nDominant Color:", dominant_color)
else:
    print("Error:", response.status_code, response.reason)
