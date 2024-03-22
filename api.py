# import
import json

import requests
from requests.auth import HTTPBasicAuth


def api(query):
    # Stock API
    url = "https://stock.adobe.io/Rest/Media/1/Search/Files"

    # Define the headers
    headers = {
        # super secret
        'x-api-key': '7f9388738de34185822e3f5c2f2ee2be',
        'x-product': 'MySampleApp',
    }

    # Define the parameters
    params = {
        # us market
        'locale': 'en_US',
        #filter premium(need to work on this one
        'search_parameters[premium]': 'true ',
        # search for dogs
        'search_parameters[words]': query,
        'result_columns[]': ['title','premium_level_id'],
    }

    # Send the request
    response = requests.get(url, headers=headers, params=params)
    # Parse the response
    return json.loads(response.text)
