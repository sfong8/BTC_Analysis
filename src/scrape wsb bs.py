import requests

url = 'https://www.reddit.com/r/wallstreetbets/search?q=daily_discussion_thread_for&restrict_sr=100'

page = requests.get(url)
page

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.findAll()[0].get_text()
# attrs = {'class': 'thing', 'data-domain': 'self.datascience'}
#
test =  soup.find_all('h3', class_ ='_eYtD2XCVieq6emjKBH3m')
#     print(post.attrs['data-domain'])
#     title = soup.find('p', class_="title")
#
