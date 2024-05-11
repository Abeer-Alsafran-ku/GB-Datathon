import requests

#function description:----------------


    {
        "name": "get_weather_info",
        "description": "Get weather information for a specific city or country, this is used for weather info only",
        "parameters": {
            "type": "object",
            "properties": {
                "country": {
                    "type": "string",
                    "description": "The country name",
                }
            },
            "required": ["country"],
        }
    },




#actual fucntion:------------------
# API used: https://weatherstack.com/
def get_weather_info(arguments):
    # Parse the JSON arguments
    params = json.loads(arguments)
    # Extract parameters
    country = params.get("country")
    # Get flight information between two locations
    params = {
    'access_key': '1200131e627f2384b5d08595338a8976',
    'query': country
    }
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    res = u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature'])
    weather_info = {
        'weather' : res
    }

    return json.dumps(weather_info)



