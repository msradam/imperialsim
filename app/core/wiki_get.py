import wikipedia
from bs4 import BeautifulSoup


def get_info(wiki_title):
	wiki_page = wikipedia.WikipediaPage(wiki_title)
	wiki_page_html = wiki_page.html()
	wiki_soup = BeautifulSoup(wiki_page_html, features="html.parser")

	wiki_lists = wiki_soup.find_all("li")

	events = []
	for event in wiki_lists:
		event_info = {}
		year = event.text[:4]
		if year.isdigit():
			year = int(year)
			if year >= 1492:
				event_info["year"] = year
				description = event.text



				event_info["description"] = description
				events.append(event_info)
	return events

colonialism_info = get_info("Chronology of Western colonialism")
print(colonialism_info)

'''
print("imperialism")
imperialism_info = get_info("Timeline of European imperialism")
print(imperialism_info)
'''