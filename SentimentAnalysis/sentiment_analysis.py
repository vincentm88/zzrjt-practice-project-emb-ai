"""Module providing a function to connect to watson api."""
import json
import requests

def sentiment_analyzer(text_to_analyse):
    """Function to  take text and send it to api"""
    url_base = "https://sn-watson-sentiment-bert.labs.skills.network"
    url_case = "/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    url = url_base + url_case
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=5)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}
