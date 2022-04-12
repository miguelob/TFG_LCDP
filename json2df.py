from curses import keyname
from email import header
from pandas import read_json
from pandas import json_normalize
import pandas as pd
import json

data = json.load(open('TEXT.json'))

df = pd.DataFrame(data["results"])

df_nested_list = pd.json_normalize(
    data["results"])

#final = df_nested_list[["is_quote_status","quote_count","reply_count","reply_count","favorite_count","user.followers_count","user.favourites_count"]]
final = df_nested_list["text"]
print(final.head())

final.to_csv('TEXT.csv')