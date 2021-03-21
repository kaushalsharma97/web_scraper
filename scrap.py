import requests
from bs4 import BeautifulSoup
import pprint 

url = 'https://news.ycombinator.com/news'
url2 = 'https://news.ycombinator.com/news?p=2'
res = requests.get(url)
res2 = requests.get(url2)

soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')

story = soup.select('.storylink')
subtext = soup.select('.subtext')

story2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_story = story+story2
mega_subtext = subtext+subtext2

def sort_by_votes(hnlist):
	return sorted(hnlist,key=lambda k:k['votes'], reverse=True)


def custom_hn(story,subtext):
	hn = []
	for idx,item in enumerate(story):
		title = item.getText()
		links = item.get('href',None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace('points',''))
			if points > 100:
				hn.append({'title':title,'links':links,'votes':points})
	return sort_by_votes(hn)

pprint.pprint(custom_hn(mega_story,mega_subtext))  