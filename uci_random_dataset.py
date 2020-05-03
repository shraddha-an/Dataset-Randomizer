# Scraping the UCI ML Repository Website for the list of datasets

# Importing libraries
import requests
import urllib.request

from bs4 import BeautifulSoup as bs

import pandas as pd, numpy as np

# Accessing the URL for List view of the dataset listings
url = 'https://archive.ics.uci.edu/ml/datasets.php?format=&task=&att=&area=&numAtt=&numIns=&type=&sort=nameUp&view=list'
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
response = requests.get(url, headers = agent)

# Parsing the HTML
soup = bs(response.text, 'html.parser')

# Saving the names of all the datasets in a list; the links are embedded within the p tags belonging to the class 'normal'
ptag_list = soup.find_all('p', class_ = 'normal')
listing = []

for link_title in ptag_list:
    listing.append(link_title.text)

# Remove those links that do not point to datasets
listing = listing[8:505]

# Extracting links
link_list = []

for link in  soup.find_all('a', href = True):
    k = 'https://archive.ics.uci.edu/ml' + '/' + link['href']
    link_list.append(k)

# Removing links which are not pointing to any dataset
link_list = link_list[38: 535]

# Merging the Dataset name & links into 1 dataframe
link_list = pd.DataFrame(link_list, columns = ['Links'])
listing = pd.DataFrame(listing, columns = ['Name'])
dataset_list = pd.concat((listing, link_list), axis = 1)

# Generate a random number between 0 & 496 for the 497 datasets present & store the link as a string
rn = np.random.randint(0, 496)
random_link = (dataset_list['Links'][rn])

