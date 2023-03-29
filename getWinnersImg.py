import urllib.request
from urllib.error import HTTPError
import os
import pandas as pd

# import data
data = pd.read_csv('https://raw.githubusercontent.com/pavlicag/campaign_finance_donation_optimization/main/Endorsements/117Legislators.csv')

# create a directory for the photos if it doesn't exist
if not os.path.exists("congress_photos"):
    os.makedirs("congress_photos")

count = 0
for bioguide_id in data['bioguide_id']:
    if not pd.isnull(bioguide_id):
        url = f'https://bioguide.congress.gov/bioguide/photo/{bioguide_id[0]}/{bioguide_id}.jpg'
        filename = f"congress_photos/{data['firstlast'][count]}.jpg"
        try:
            urllib.request.urlretrieve(url, filename)
        except HTTPError:
            print(f"Error downloading image for {data['firstlast'][count], bioguide_id}")
        count += 1
    else:
        count += 1
