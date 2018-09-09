import config
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, SentimentOptions#, ConceptsOptions, CategoriesOptions
#import pycountry

#countries = (pycountry.countries)
#historic_countries = (pycountry.historic_countries)

'''
try:
	pycountry.countries.get(name="as")
except KeyError:
	print("oops")
'''

natural_language_understanding = NaturalLanguageUnderstandingV1(
		version='2018-03-16',
	    username=config.NLU_USER,
	    password=config.NLU_PASS,
	    url=config.NLU_URL
	)

def find_countries(text):
	response = natural_language_understanding.analyze(
	  text=text,
	  features=Features(
	  	entities=EntitiesOptions(
	  		limit=3
	  	),
	  	sentiment=SentimentOptions(
	  		)
	  )
	)
	#print(response)

	ent = []
	for i in response["entities"]:
		#ent.append(i["text"])
		try:
			if i["type"] == 'Location':
				ent.append(i["text"])
		except:
			continue
	return ent

def find_sentiment(text):
	response = natural_language_understanding.analyze(
	  text=text,
	  features=Features(
	  	sentiment=SentimentOptions(
	  	)
	  )
	)
	sent_score = response["sentiment"]["document"]["score"]
	return sent_score

#sentence = '1492: "Discovery" of the "New World" and symbolic date of the European Age of Exploration; beginning of the colonization of the Americas and of the Columbian Exchange'
#print(find_countries(sentence))
#print(find_sentiment(sentence))
