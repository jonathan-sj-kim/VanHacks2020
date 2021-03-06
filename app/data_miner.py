import time
import numpy as np
import requests
import json
import csv

# restaurant_name = []
# restaurant_add = []
# restaurant_cuisine = []
# restaurant_ranking = []
# restaurant_rating = []
# serving_time = []
# price_range = []
# review_num = []
# visit_year = []
# visit_month = []
# review_year = []
# review_month = []
# review_day = []
# overall_rating = []
# value = []
# service = []
# food = []
# review_title = []
# review_content = []
# lat = []
# lon = []
HEADERS = {
    'Authorization': 'Bearer oaLwG_o_UYW2jDX6plx8ON5aa1SlH_TOe7_TQ-UKNQJkMUUvwMPIDF1CKbhmjhoQc14a6D_Ui_OFSMRHafDHAR0bW55OBBzhONjXwH2Dph190Ey-QwV6Q3Esmn5vX3Yx',
    'content-type': 'applications/json',
    'ratelimit-dailylimit': '5000'
}
ENDPOINT = "https://api.yelp.com/v3/businesses/search"
PARAMETERS = {
    'location': '4195 Alexandra St, Vancouver, BC V6J 4C6',
    'offset': 0,
    'radius': 40000,
    'limit': 50
}

# for j in range(-5, 5):
#     lon.append(float(-123.1126 + float(j/200)))
#     lat.append(float(49.2418 + float(j/200)))
# lon = np.unique(np.array(lon))
# lat = np.unique(np.array(lat))

with open('data/Restaurant_links.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['id', 'name', 'url', 'city', 'zip_code', 'biz_rating', 'categories', 'price'])
    for i in range(20):
        try:
            PARAMETERS['offset'] = i * 50
            r = requests.get(url = ENDPOINT, params = PARAMETERS, headers=HEADERS)
            json_loaded = json.loads(r.text)
            print(len(json_loaded['businesses']))
            if json_loaded['businesses'] is None or len(json_loaded['businesses']) < 1:
                break
            for business in json_loaded['businesses']:
                price = ""
                if 'price' in business.keys():
                    price = business['price']
                csv_writer.writerow([business['id'], business['name'],
                                    business['url'], business['location']['city'],
                                    business['location']['zip_code'], 
                                    business['rating'],
                                    business['categories'],
                                    price
                                    ])
        except:
            print("failed, moving on.")
            break
