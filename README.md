This repository contains Python scripts that automate text translation using AWS Translate and Google Cloud Translate services. The scripts can be run as standalone Python programs or deployed as AWS Lambda functions. There are two separate scripts included in the repository, each utilizing a different translation service.

## AWS Translation

The `translateAWS.py` script demonstrates how to translate text stored in an S3 object using AWS Translate. It uses the Boto3 library to interact with AWS services, specifically Amazon S3 and Amazon Translate. The translated text is then saved back to the S3 bucket for further use.

### Prerequisites

- Python 3.x
- Boto3 library
- AWS CLI configured with appropriate access and secret keys

### Usage

1. Configure AWS CLI with your AWS access and secret keys.
2. Customize the translation source and target languages by modifying the `lambda_handler` function in `aws_translation.py`.
3. Run the script either as a standalone Python program or deploy it as an AWS Lambda function triggered by S3 events.

## Google Cloud Translation

The `translateGCP.py` script demonstrates how to translate text extracted from a PDF file using the Google Cloud Translate API. It uses the `translate_v2` library from the `google.cloud` package to interact with the Google Cloud Translation service. The translated text is saved to an output file.

### Prerequisites

- Python 3.x
- `google-cloud-translate` library
- Google Cloud Translation API credentials

### Usage

1. Install the `google-cloud-translate` library using pip: `pip install google-cloud-translate`.
2. Obtain the Google Cloud Translation API credentials file in JSON format.
3. Customize the `pdf_filename`, `target_language`, and `output_filename` variables in `google_cloud_translation.py` according to your requirements.
4. Run the script as a standalone Python program.


# Image Analysis with Azure Cognitive Services

This Python script demonstrates how to perform image analysis using Azure Cognitive Services API. The script analyzes an image provided via a URL and retrieves information such as categories, description, and dominant color.

## Prerequisites

- Python 3.x
- `requests` library

## Setup

1. Obtain an Azure Cognitive Services API endpoint and subscription key for the Vision service.
2. Replace the `endpoint` and `subscription_key` variables in the script with your own values.
3. Provide the URL of the image you want to analyze by replacing the `image_url` variable.
4. Install the `requests` library if you haven't already by running `pip install requests`.

## Usage

1. Run the script using Python.
2. The script will send a POST request to the Azure Cognitive Services API, providing the image URL and request parameters.
3. The API will analyze the image and return the results in the response.
4. If the response status code is 200 (OK), the script will extract and print the following information:
   - Categories: The categories or objects detected in the image.
   - Description: A caption or description of the image.
   - Dominant Color: The dominant color in the image.
5. If there is an error, the script will print the response status code and reason.



# Text Sentiment Analysis with Azure Cognitive Services

This Python script demonstrates how to perform text sentiment analysis using Azure Cognitive Services API. The script analyzes the sentiment of provided texts and returns sentiment scores and labels.

## Prerequisites

- Python 3.x
- `requests` library

## Setup

1. Obtain an Azure Cognitive Services API endpoint and subscription key for the Text Analytics service.
2. Replace the `endpoint` and `subscription_key` variables in the script with your own values.
3. Update the `data` variable with the texts you want to analyze. Each document should include a unique `id`, `language`, and `text`.
4. Install the `requests` library if you haven't already by running `pip install requests`.

## Usage

1. Run the script using Python.
2. The script will send a POST request to the Azure Cognitive Services API, providing the texts and request parameters.
3. The API will analyze the sentiment of the texts and return the results in the response.
4. If the response status code is 200 (OK), the script will extract and print the following information for each document:
   - Document ID: The identifier of the document.
   - Sentiment: The sentiment label of the text (Positive or Negative).
   - Score: The sentiment score indicating the confidence level (ranging from 0 to 1).
5. If there is an error, the script will print the response status code and reason.





