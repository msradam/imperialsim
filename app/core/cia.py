import requests
import json

response = json.loads(requests.get("https://raw.githubusercontent.com/iancoleman/cia_world_factbook_api/master/data/factbook.json").text)

list_of_countries = ["india", "iran", "philippines","nigeria","vietnam"]

d0 = [{'india': \
{u'population_without_electricity': \
{u'units': u'people', u'value': 237400000}, u'total_electrification': {u'units': u'%', u'value': 79}, u'urban_electrification': {u'units': u'%', u'value': 98}, u'date': u'2013', u'rural_electrification': {u'units': u'%', u'value': 70}}
}]


def get_stats(country):
	d = {}
	d[country] = []
	d[country].append(response["countries"][country]["data"]["energy"]["electricity"]["access"])
	d[country].append(response["countries"][country]["data"]["people"]["life_expectancy_at_birth"]
		)
	d[country].append(response["countries"][country]["data"]["people"]["infant_mortality_rate"])
	return d

country_energy_access = list(map(get_stats, list_of_countries))
print(country_energy_access)

#income = response["countries"]["argentina"]["data"]["economy"]["household_income_by_percentage_share"]
#print(income)