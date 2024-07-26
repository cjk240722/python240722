import requests
import pandas as pd

# URL to fetch the JSON data
url = r"https://m.land.naver.com/cluster/ajax/articleList?itemId=21221110&mapKey=&lgeo=21221110&showR0=&rletTpCd=APT&tradTpCd=A1&z=12&lat=37.5710486&lon=127.0641673&btm=37.4480865&lft=126.9949877&top=37.693808&rgt=127.1333468&totCnt=1562&sort=rank&page=6"

# Fetch the JSON data from the URL
response = requests.get(url)
data = response.json()

# Extracting relevant information from the JSON data
items = data.get('body', {}).get('list', [])

# Convert the data into a DataFrame
df = pd.DataFrame(items)

# Saving the DataFrame to an Excel file
df.to_excel("naver_real_estate_page_6.xlsx", index=False)

print("Data has been written to naver_real_estate_page_6.xlsx")
