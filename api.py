# import
import json
from key import apikey
import requests



def api(query):
    # Stock API
    url = "https://stock.adobe.io/Rest/Media/1/Search/Files"

    # Define the headers
    headers = {
        # super secret
        'x-api-key': apikey,
        'x-product': 'MySampleApp',
    }

    # Define the parameters
    params = {
        # us market
        'locale': 'en_US',
        # filter premium(need to work on this one
        'search_parameters[filters][premium]': 'true',
        # search for dogs
        'search_parameters[words]': query,
        'result_columns[]': ['title', 'premium_level_id', 'is_premium'],
        'search_parameters[limit]': 100,
    }

    # Send the request
    response = requests.get(url, headers=headers, params=params)
    # Parse the response
    return json.loads(response.text)
