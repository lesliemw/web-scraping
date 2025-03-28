import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/', timeout=10)
response2 = requests.get('https://news.ycombinator.com/?p=2', timeout=10)

combined = response.text + response2.text
soup = BeautifulSoup(combined, 'html.parser')

links = soup.select(".titleline")
subtext = soup.select(".subtext")


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, vote):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


print(create_custom_hn(links, subtext))
