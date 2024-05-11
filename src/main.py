# ## this is a main file for python

# import requests

# def search_wikipedia(query):
#     url = "https://en.wikipedia.org/w/api.php"
#     params = {
#         "action": "query",
#         "format": "json",
#         "list": "search",
#         "srsearch": query
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     if 'error' in data:
#         print("Error:", data['error']['info'])
#         return None

#     search_results = data['query']['search']
#     if not search_results:
#         print("No results found.")
#         return None

#     return search_results

# def get_page_content(title):
#     url = "https://en.wikipedia.org/w/api.php"
#     params = {
#         "action": "query",
#         "format": "json",
#         "prop": "extracts",
#         "titles": title,
#         "exintro": True
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     if 'error' in data:
#         print("Error:", data['error']['info'])
#         return None

#     pages = data['query']['pages']
#     page_id = next(iter(pages))
#     if page_id == "-1":
#         print("Page not found.")
#         return None

#     page_content = pages[page_id]['extract']
#     return page_content

# # Example usage:
# search_query = input("Enter search query: ")
# search_results = search_wikipedia(search_query)

# if search_results:
#     print("Search Results:")
#     for result in search_results:
#         print("-", result['title'])

#     selected_title = input("Enter the title of the page you want to view: ")
#     page_content = get_page_content(selected_title)

#     if page_content:
#         print("\nPage Content:")
#         print(page_content)



import requests

def flight_api(origin,target):
    params = {
    'access_key': 'f1d23ab03a88741c8ba97af68561247e'
    }
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    api_response = api_result.json()
    
    for flight in api_response['data']:

        if target.lower() in str(flight['arrival']['airport']).lower() and origin.lower() in str(flight['departure']['airport']).lower() :
            print( u'%s flight %s from %s (%s) and time =%s to %s (%s) ' %(
                flight['airline']['name'],
                flight['flight']['iata'],
                flight['departure']['airport'],
                flight['departure']['iata'],
                flight['departure']['scheduled'],
                flight['arrival']['airport'],
                flight['arrival']['iata']))
flight_api('Yantai','Seoul')

        


