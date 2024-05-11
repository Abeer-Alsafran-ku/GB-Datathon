#function description:----------------


    {
        "name": "get_flight_info",
        "description": "Get flight information between two locations, this is used for flight info only, not booking, destination",
        "parameters": {
            "type": "object",
            "properties": {
                "loc_origin": {
                    "type": "string",
                    "description": "The departure country",
                },
                "loc_destination": {
                    "type": "string",
                    "description": "The destination country",
                },
            },
            "required": ["loc_origin", "loc_destination"],
        }
    },




#actual fucntion:------------------

def get_flight_info(arguments):
    # Parse the JSON arguments
    params = json.loads(arguments)
    # Extract parameters
    loc_origin = params.get("loc_origin")
    loc_destination = params.get("loc_destination")

    # Get flight information between two locations
    # api key
    params = {
    'access_key': 'f1d23ab03a88741c8ba97af68561247e'
    }
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    api_response = api_result.json()
    flag = True
    for flight in api_response['data']:
        if loc_destination.lower() in str(flight['arrival']['airport']).lower() and loc_origin.lower() in str(flight['departure']['airport']).lower() :
            mystr =  u'%s flight %s from %s (%s) and time = %s to %s (%s) ' %(
                flight['airline']['name'],
                flight['flight']['iata'],
                flight['departure']['airport'],
                flight['departure']['iata'],
                flight['departure']['scheduled'],
                flight['arrival']['airport'],
                flight['arrival']['iata'])
            flag = True
            break
        else:
            flag= False
    if flag:
        flight_info = {
            'info' : mystr
        }
    else:
        mystr  = 'Sorry, I could not find a flight for your exact request.'
        flight_info = {
            'info' : mystr
        }
    return json.dumps(flight_info)
