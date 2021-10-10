from bs4 import BeautifulSoup
import requests
import pandas as pd

source=requests.get('https://www.vlr.gg/event/stats/466/valorant-champions-tour-stage-3-masters-berlin').text

soup = BeautifulSoup(source,'lxml')

table = soup.find('table', {'class':'wf-table mod-stats'})

headers = []

for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

df = pd.DataFrame(columns=headers)

for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data

print(df)
df = pd.DataFrame(df)
df.to_csv('table.csv')
print("saved to file")
