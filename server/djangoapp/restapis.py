import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth

def get_request(url, apikey=None, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        if api_key:
            # Basic authentication GET
            response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs, auth=HTTPBasicAuth('apikey', api_key))
        else:
            # no authentication GET
            response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer["doc"]
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
    json_result = get_req(url, dealerId=dealer_id)
    if json_result:
        reviews = json_result["entries"]
        for review in reviews:
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
    return results

def analyze_review_sentiments(text):
    result = "Not checked"
    try:
        json_result = get_req(url="https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/d85d806f-e15e-4ce8-bb21-1e00d7599efb", 
                        api_key="3C-C5VxleVs35gUPBUSZ2q2TedaEjDI5OyTznE8iWEF5", 
                        version="2021-03-25",
                        features="sentiment",
                        text=urllib.parse.quote_plus(text))
        result = json_result["sentiment"]["document"]["label"]
    finally:
        return result

