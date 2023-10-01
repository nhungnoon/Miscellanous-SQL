"""
Quick mock up on
(1) get information from pre-saved html
(2) generate sqlite3 database with mockup data
"""
import json
import scrapy
import sqlite3
import pandas as pd
# save html for List of Cities in Vietnam
# based on https://en.wikipedia.org/wiki/List_of_cities_in_Vietnam
saved_local_url = "List of cities in Vietnam - Wikipedia.html"

with open(saved_local_url) as _f:
    url_data = _f.read()
response = scrapy.http.TextResponse(
    saved_local_url, 
    body=url_data, 
    encoding='utf-8'
    )
# Extract data for available province/city
table = response.xpath('//table').xpath('tbody')

# Save data as json file
data_province = {}
for tr in table.xpath('tr'):
    province = tr.xpath('td/a/text()').extract()
    if len(province) == 2:
        data_province[province[0]] = province[1]


# Dumping data to json file
with open("cities_vietnam.json", "w") as _f:
    json.dump(data_province, _f)


# Save data as csv file
data_province = []
for tr in table.xpath('tr'):
    province = tr.xpath('td/a/text()').extract()
    if len(province) == 2:
        data_province.append(province)

# Save data to csv
data_province = pd.DataFrame(data_province)
data_province.columns = ['name', 'province']
data_province.to_csv("cities_vietnam.csv")


# Create a database sqlite3
def create_mock_database(name: str = 'cities_vietnam.db'):
    connection = sqlite3.connect(name)
    db_table = 'CREATE TABLE results (id integer primary key, city_name TEXT, province TEXT)'
    cursor = connection.cursor()
    cursor.execute(db_table)
    connection.commit()
#create_mock_database()

# insert results into the newly created database
connection = sqlite3.connect("cities_vietnam.db")
cursor = connection.cursor()
query = 'INSERT INTO results(city_name, province) VALUES(?, ?)'

for tr in table.xpath('tr'):
    province = tr.xpath('td/a/text()').extract()
    if len(province) == 2:
        city_name = province[0]
        province = province[1]
        cursor.execute(query, (city_name, province)) 
        connection.commit()
