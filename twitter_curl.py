import json
import requests
import pandas as pd


url = 'https://api.twitter.com/1.1/tweets/search/fullarchive/prod.json'
head = {'authorization': 'Bearer PLACE_HERE_THE_BEARER',
           'content-type': 'application/json'}
dat = {
                "query":"#LCDP berlin",
                "maxResults": "100",
                "fromDate":"201703010000", 
                "toDate":"202203010000"
                }


response = requests.post(url, headers=head, data=json.dumps(dat))
data = json.loads(response.content.decode(response.encoding))
savejson = json.dumps(data)
datos = savejson[1:-1]
writejson = open('TEXT.json', 'w')
writejson.write(savejson)
data = json.load(open('TEXT.json'))

df = pd.DataFrame(data["results"])

df_nested_list = pd.json_normalize(
    data["results"])
print(df_nested_list)
df_nested_list.to_csv('TEXT.csv')