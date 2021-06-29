import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    #response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
    response={}
    try:
        response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
        status_code = response.status_code
        print("With status {} ".format(status_code))
        print(response.text)
        json_data = json.loads(response.text)
        return json_data
        #if api_key:
        #    # Basic authentication GET
        #    response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs, auth=HTTPBasicAuth('apikey', api_key))
        #else:
        #    # no authentication GET
        #    response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
        status_code = "Network exception occurred"
        print("With status {} ".format(status_code))
        return response

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, json_payload, **kwargs):
    print(kwargs)
    try:
        response = requests.post(url, json=json_payload, params=kwargs)
    except:
        print("Something went wrong")
    print (response)
    return response


def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["entries"]
        # For each dealer object
        for dealer in dealers:
            dealer_doc = dealer
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results


def get_dealer_by_id_from_cf(url, dealer_id):
    json_result = get_req(url, id=dealer_id)

    if json_result:
        dealers = json_result["entries"]
        for dealer in dealers:
            dealer_obj = CarDealer(address=dealer["address"], city=dealer["city"], full_name=dealer["full_name"],
                                   id=dealer["id"], lat=dealer["lat"], long=dealer["long"],
                                   short_name=dealer["short_name"],state=dealer["state"],
                                   st=dealer["st"], zip=dealer["zip"])
            return dealer_obj

    return None


def get_dealer_reviews_from_cf(url, dealer_id):
    results = []
    json_result = get_request(url, dealerId=dealer_id)
    if json_result:
        reviews = json_result["entries"]
        for review in reviews:
            if dealer_id == review["dealership"]:
                if review["purchase"]:
                    review_obj = DealerReview(make=review["car_make"], model=review["car_model"], 
                                        year=review["car_year"], dealer_id=review["dealership"], 
                                        id=review["id"], name=review["name"], purchase=review["purchase"], 
                                        purchase_date=review["purchase_date"], review=review["review"])
                else:
                    review_obj = DealerReview(dealer_id=review["dealership"], 
                                        id=review["id"], name=review["name"], purchase=review["purchase"], 
                                        review=review["review"])
                review_obj.sentiment = analyze_review_sentiments(review_obj.review)
                results.append(review_obj)
    print(results)
    return results

def analyze_review_sentiments(text):
    result = "Not checked"
    api_key = "3C-C5VxleVs35gUPBUSZ2q2TedaEjDI5OyTznE8iWEF5"
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/d85d806f-e15e-4ce8-bb21-1e00d7599efb"
    authenticator = IAMAuthenticator(api_key)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version = "2021-03-25",
        authenticator = authenticator
    )
    natural_language_understanding.set_service_url(url)
    response = natural_language_understanding.analyze(
        text = text,
        features = Features(sentiment = SentimentOptions())
    ).get_result()
    print(json.dumps(response))
    sentiment_score = str(response["sentiment"]["document"]["score"])
    sentiment_label = response["sentiment"]["document"]["label"]
    print(sentiment_score)
    print(sentiment_label)
    sentimentresult = sentiment_label
    return sentimentresult

