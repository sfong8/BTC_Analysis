import requests

url = 'https://www.reddit.com/r/wallstreetbets/search?q=daily_discussion_thread_for'

# page = requests.get(url)
# page
def flag_inDate(x,y):
    z=False
    for certain_date in list(y['date2']):
        # print(certain_date)
        if str(certain_date) in str(x):
            z=True
            break
    return z


from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.findAll()[0].get_text()
# attrs = {'class': 'thing', 'data-domain': 'self.datascience'}
#

#     print(post.attrs['data-domain'])
#     title = soup.find('p', class_="title")
#
import pandas as pd
from datetime import datetime
from selenium import webdriver

driver = webdriver.Chrome(r'/Users/simonfong/Downloads/chromedriver')
driver.get(url)
total_height = int(driver.execute_script("return document.body.scrollHeight"))
# import time
# for i in range(1, total_height, 500):
#     if driver.execute_script("return document.body.scrollHeight")==0:
#         break
#     else:
#         driver.execute_script("window.scrollTo(0, {});".format(i))
#         time.sleep(5)

# test = driver.find_element_by_xpath("/html/body/div/article/section[1]/div[2]/dl/dd[1]/a").
pageSource = driver.page_source

soup = BeautifulSoup(pageSource, 'html.parser')
import time
time.sleep(5)
test =  soup.find_all('h3', class_ ='_eYtD2XCVieq6emjKBH3m')

# /Users/simonfong/PycharmProjects/BTC_Analysis/src/reddit_wsb.csv
import os

##get the subid
y=pd.DataFrame(pd.date_range(start="2021-01-20",end="2021-02-10"))
y.columns= ['date']
y['date2'] = y['date'].apply(lambda x:datetime.strftime(x,'%B %d, %Y'))


'/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]'
# //*[@id="t3_la0n4z"]/div[2]/div/div[2]/div[1]/div[1]/a/div/h3
# /html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[4]/div/div/div[2]/div/div[2]/div[1]/div[1]/a/div/h3
#
# //*[@id="t3_l7wqsm"]/div[2]/div/div[2]/div[1]/div[1]/a/div/h3
# /html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[6]/div/div/div[2]/div/div[2]/div[1]/div[1]/a/div/h3
counter = 0
# elems = driver.find_elements_by_class_name('_eYtD2XCVieq6emjKBH3m')
elems = driver.find_elements_by_class_name('_2INHSNB8V5eaWp4P0rY_mE')
sub_id =[]
# elem = elems[0]

def extract_subID(x):
    x=str(x)
    x2=x.split("https://www.reddit.com/r/wallstreetbets/comments/")[1]
    x3 = x2.split('/daily_discussion_thread_for')[0]
    return x3
counter2= 0
for elem in elems:
    print('counter2',counter2)
    counter2+=1
    x = elem.find_elements_by_tag_name('span')[0].text
    if flag_inDate(x,y):
        counter+=1
        x2 = elem.get_attribute('href')
        if x2 is None:

        #x2 = elem.find_elements_by_tag_name('')
            x2= elem.find_elements_by_class_name('SQnoC3ObvgnGjWt90zD9Z')[0].get_attribute('href')

        sub_id.append(extract_subID(x2))


import csv

with open('sub_id.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(sub_id)

# x = elem.find_elements_by_tag('h3')
# x = str(elem)
