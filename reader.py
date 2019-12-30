import requests
from bs4 import BeautifulSoup
from random import randint
import webbrowser

# Get a Response object from Real Python and parse the content.
r = requests.get('https://realpython.com')
soup = BeautifulSoup(r.text, 'html.parser')


# Filter the articles.
articles = soup.find_all('div', class_='card border-0')


# Retrieve a random article.
def get_article():
	article = randint(0, len(articles) - 1)
	link_to_article = articles[article].a['href']
	return link_to_article


# Launch the program and glean some random Python knowledge. :)
if __name__ == '__main__':
	slug = get_article()
	url = 'https://realpython.com%s' % slug
	webbrowser.open(url)