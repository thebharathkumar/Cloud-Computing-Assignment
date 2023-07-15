AWS Translation:
The translateAWS.py script demonstrates how to translate text stored in an Amazon S3 object using AWS Translate. It utilizes the Boto3 library to interact with AWS services, specifically Amazon S3 and Amazon Translate. The translated text is then saved back to the S3 bucket for further use.

Prerequisites:

Python 3.x
Boto3 library
AWS CLI configured with appropriate access and secret keys
Usage:

Configure AWS CLI with your AWS access and secret keys.
Customize the translation source and target languages by modifying the lambda_handler function in aws_translation.py.
Run the script either as a standalone Python program or deploy it as an AWS Lambda function triggered by S3 events.
Google Cloud Translation:
The translateGCP.py script demonstrates how to translate text extracted from a PDF file using the Google Cloud Translate API. It relies on the translate_v2 library from the google.cloud package to interact with the Google Cloud Translation service. The translated text is then saved to an output file.

Prerequisites:

Python 3.x
google-cloud-translate library
Google Cloud Translation API credentials in JSON format
Usage:

Install the google-cloud-translate library using pip: pip install google-cloud-translate.
Obtain the Google Cloud Translation API credentials file in JSON format.
Customize the pdf_filename, target_language, and output_filename variables in google_cloud_translation.py according to your requirements.
Run the script as a standalone Python program.
Image Analysis with Azure Cognitive Services:
This Python script demonstrates how to perform image analysis using Azure Cognitive Services API. The script analyzes an image provided via a URL and retrieves information such as categories, description, and dominant color.

Prerequisites:

Python 3.x
requests library
Setup:

Obtain an Azure Cognitive Services API endpoint and subscription key for the Vision service.
Replace the endpoint and subscription_key variables in the script with your own values.
Provide the URL of the image you want to analyze by replacing the image_url variable.
Install the requests library if you haven't already by running pip install requests.
Usage:

Run the script using Python.
The script will send a POST request to the Azure Cognitive Services API, providing the image URL and request parameters.
The API will analyze the image and return the results in the response.
If the response status code is 200 (OK), the script will extract and print information such as Categories, Description, and Dominant Color.
If there is an error, the script will print the response status code and reason.
Text Sentiment Analysis with Azure Cognitive Services:
This Python script demonstrates how to perform text sentiment analysis using Azure Cognitive Services API. The script analyzes the sentiment of provided texts and returns sentiment scores and labels.

Prerequisites:

Python 3.x
requests library
Setup:

Obtain an Azure Cognitive Services API endpoint and subscription key for the Text Analytics service.
Replace the endpoint and subscription_key variables in the script with your own values.
Update the data variable with the texts you want to analyze. Each document should include a unique id, language, and text.
Install the requests library if you haven't already by running pip install requests.
Usage:

Run the script using Python.
The script will send a POST request to the Azure Cognitive Services API, providing the texts and request parameters.
The API will analyze the sentiment of the texts and return the results in the response.
If the response status code is 200 (OK), the script will extract and print information such as Document ID, Sentiment, and Score for each document.
If there is an error, the script will print the response status code and reason.
