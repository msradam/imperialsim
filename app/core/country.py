import config
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions#, ConceptsOptions, CategoriesOptions
import pycountry

countries = (pycountry.countries)
historic_countries = (pycountry.historic_countries)

try:
	pycountry.countries.get(name="as")
except KeyError:
	print("oops")


def find_countries(text):

	natural_language_understanding = NaturalLanguageUnderstandingV1(
		version='2018-03-16',
	    username=config.NLU_USER,
	    password=config.NLU_PASS,
	    url=config.NLU_URL
	)

	response = natural_language_understanding.analyze(
	  text=text,
	  features=Features(
	  	entities=EntitiesOptions(
	  		limit=3)
	    )
	  )
	print(response)
	ent = []
	for i in response:
		if i == "entities":
			for j in response[i]:
				ent.append(j["text"])
	return ent

sentence = "Franco-Prussian War"
print(find_countries(sentence))

