import requests
from django.http import JsonResponse
from bs4 import BeautifulSoup

def extract_search_results(html):
    soup = BeautifulSoup(html, "html.parser")
    
    div = soup.find("div", {"class": "rg_i"})
    
    url = div.a["href"]
    title = div.a.img["alt"]
    
    result = {"url": url, "title": title}
    return result


def candidate_info(request, cid):
    '''
    retrieves candidate summary info from opensecrets
    param request:  HTTP request
    param cid: candidates ID as string
    returns JSON of candidate info 
    
    '''
    api_key = 'a8e83e298612f39c35ba6b9765e24149'

    api_url = f'https://www.opensecrets.org/api/?method=candSummary&cid={cid}&apikey={api_key}&output=json'

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        candidate_summary = data['response']['summary']

        return JsonResponse(candidate_summary)

    else:
        return JsonResponse({'error': 'Candidate information not found'}, status=404)
    
def get_candidate_website(cid):
    """
    Retrieves the website of a candidate with the specified CID using the OpenSecrets API.

    :param cid: The candidate ID (CID) as a string.
    :return: The candidate's website as a string, or None if not found.
    """
    api_key = 'a8e83e298612f39c35ba6b9765e24149'
    api_url = f'https://www.opensecrets.org/api/?method=candSummary&cid={cid}&apikey={api_key}&output=json'

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        candidate_summary = data['response']['summary']
        website = candidate_summary.get('website', None)
        return website
    else:
        raise Exception(f'Error retrieving candidate website: {response.status_code}')


def candidate_images(query):
    '''
    Note: As a further work, it would be nice to have a more image filtering process.

    param query: string of key words that will be used as a google search query I.E "Name, party, district, professional headshot."
    
    returns dictionary of a candidate image with there url as dictionary
    '''
    url = "https://www.google.com/search?q={}&tbm=isch".format(query)
    
    
    response = requests.get(url)
    
    if response.status_code == 200:
        candidate_image = extract_search_results(response.text)
        
        
        return candidate_image
    else:
        return []