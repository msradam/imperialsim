import json


country_map = {
	"AF": "Afghanistan",
	"AO": "Angola",
	"AL": "Albania",
	"AE": "United Arab Emirates",
	"AR": "Argentina",
	"AM": "Armenia",
	"AU": "Australia",
	"AT": "Austria",
	"AZ": "Azerbaijan",
	"BI": "Burundi",
	"BE": "Belgium",
	"BJ": "Benin",
	"BF": "Burkina Faso",
	"BD": "Bangladesh",
	"BG": "Bulgaria",
	"BA": "Bosnia and Herzegovina",
	"BY": "Belarus",
	"BZ": "Belize",
	"BO": "Bolivia",
	"BR": "Brazil",
	"BN": "Brunei Darussalam",
	"BT": "Bhutan",
	"BW": "Botswana",
	"CF": "Central African Republic",
	"CA": "Canada",
	"CH": "Switzerland",
	"CL": "Chile",
	"CN": "China",
	"CI": "Côte d'Ivoire",
	"CM": "Cameroon",
	"CD": "Democratic Republic of the Congo",
	"CG": "Republic of Congo",
	"CO": "Colombia",
	"CR": "Costa Rica",
	"CU": "Cuba",
	"CZ": "Czech Republic",
	"DE": "Germany",
	"DJ": "Djibouti",
	"DK": "Denmark",
	"DO": "Dominican Republic",
	"DZ": "Algeria",
	"EC": "Ecuador",
	"EG": "Egypt",
	"ER": "Eritrea",
	"EE": "Estonia",
	"ET": "Ethiopia",
	"FI": "Finland",
	"FJ": "Fiji",
	"GA": "Gabon",
	"GB": "United Kingdom",
	"GE": "Georgia",
	"GH": "Ghana",
	"GN": "Guinea",
	"GM": "The Gambia",
	"GW": "Guinea-Bissau",
	"GQ": "Equatorial Guinea",
	"GR": "Greece",
	"GL": "Greenland",
	"GT": "Guatemala",
	"GY": "Guyana",
	"HN": "Honduras",
	"HR": "Croatia",
	"HT": "Haiti",
	"HU": "Hungary",
	"ID": "Indonesia",
	"IN": "India",
	"IE": "Ireland",
	"IR": "Iran",
	"IQ": "Iraq",
	"IS": "Iceland",
	"IL": "Israel",
	"IT": "Italy",
	"JM": "Jamaica",
	"JO": "Jordan",
	"JP": "Japan",
	"KZ": "Kazakhstan",
	"KE": "Kenya",
	"KG": "Kyrgyzstan",
	"KH": "Cambodia",
	"KR": "Republic of Korea",
	"XK": "Kosovo",
	"KW": "Kuwait",
	"LA": "Lao PDR",
	"LB": "Lebanon",
	"LR": "Liberia",
	"LY": "Libya",
	"LK": "Sri Lanka",
	"LS": "Lesotho",
	"LT": "Lithuania",
	"LU": "Luxembourg",
	"LV": "Latvia",
	"MA": "Morocco",
	"MD": "Moldova",
	"MG": "Madagascar",
	"MX": "Mexico",
	"MK": "Macedonia",
	"ML": "Mali",
	"MM": "Myanmar",
	"ME": "Montenegro",
	"MN": "Mongolia",
	"MZ": "Mozambique",
	"MR": "Mauritania",
	"MW": "Malawi",
	"MY": "Malaysia",
	"NA": "Namibia",
	"NE": "Niger",
	"NG": "Nigeria",
	"NI": "Nicaragua",
	"NL": "Netherlands",
	"NO": "Norway",
	"NP": "Nepal",
	"NZ": "New Zealand",
	"OM": "Oman",
	"PK": "Pakistan",
	"PA": "Panama",
	"PE": "Peru",
	"PH": "Philippines",
	"PG": "Papua New Guinea",
	"PL": "Poland",
	"KP": "Dem. Rep. Korea",
	"PT": "Portugal",
	"PY": "Paraguay",
	"PS": "Palestine",
	"QA": "Qatar",
	"RO": "Romania",
	"RU": "Unnamed",
	"RW": "Rwanda",
	"EH": "Western Sahara",
	"SA": "Saudi Arabia",
	"SD": "Sudan",
	"SS": "South Sudan",
	"SN": "Senegal",
	"SL": "Sierra Leone",
	"SV": "El Salvador",
	"RS": "Serbia",
	"SR": "Suriname",
	"SK": "Slovakia",
	"SI": "Slovenia",
	"SE": "Sweden",
	"SZ": "Swaziland",
	"SY": "Syria",
	"TD": "Chad",
	"TG": "Togo",
	"TH": "Thailand",
	"TJ": "Tajikistan",
	"TM": "Turkmenistan",
	"TL": "Timor-Leste",
	"TN": "Tunisia",
	"TR": "Turkey",
	"TW": "Taiwan",
	"TZ": "Tanzania",
	"UG": "Uganda",
	"UA": "Ukraine",
	"UY": "Uruguay",
	"US": "United States",
	"UZ": "Uzbekistan",
	"VE": "Venezuela",
	"VN": "Vietnam",
	"VU": "Vanuatu",
	"YE": "Yemen",
	"ZA": "South Africa",
	"ZM": "Zambia",
	"ZW": "Zimbabwe",
	"SO": "Somalia",
	"GF": "France",
	"FR": "France",
	"ES": "Spain",
	"AW": "Aruba",
	"AI": "Anguilla",
	"AD": "Andorra",
	"AG": "Antigua and Barbuda",
	"BS": "Bahamas",
	"BM": "Bermuda",
	"BB": "Barbados",
	"KM": "Comoros",
	"CV": "Cape Verde",
	"KY": "Cayman Islands",
	"DM": "Dominica",
	"FK": "Falkland Islands",
	"FO": "Faeroe Islands",
	"GD": "Grenada",
	"HK": "Hong Kong",
	"KN": "Saint Kitts and Nevis",
	"LC": "Saint Lucia",
	"LI": "Liechtenstein",
	"MF": "Saint Martin (French)",
	"MV": "Maldives",
	"MT": "Malta",
	"MS": "Montserrat",
	"MU": "Mauritius",
	"NC": "New Caledonia",
	"NR": "Nauru",
	"PN": "Pitcairn Islands",
	"PR": "Puerto Rico",
	"PF": "French Polynesia",
	"SG": "Singapore",
	"SB": "Solomon Islands",
	"ST": "São Tomé and Principe",
	"SX": "Saint Martin (Dutch)",
	"SC": "Seychelles",
	"TC": "Turks and Caicos Islands",
	"TO": "Tonga",
	"TT": "Trinidad and Tobago",
	"VC": "Saint Vincent and the Grenadines",
	"VG": "British Virgin Islands",
	"VI": "United States Virgin Islands",
	"CY": "Cyprus",
	"RE": "Reunion (France)",
	"YT": "Mayotte (France)",
	"MQ": "Martinique (France)",
	"GP": "Guadeloupe (France)",
	"CW": "Curaco (Netherlands)",
	"IC": "Canary Islands (Spain)"
}

my_dict2 = dict((y,x) for x,y in country_map.items())

data = [{'year': 1492, 'description': '1492: "Discovery" of the "New World" and symbolic date of the European Age of Exploration; beginning of the colonization of the Americas and of the Columbian Exchange', 'countries': ['Americas'], 'sentiment': 0.0}, {'year': 1493, 'description': '1493: Papal Bull Inter caetera on May 4', 'countries': [], 'sentiment': 0.0}, {'year': 1494, 'description': "1494: Treaty of Tordesillas dividing the world outside of Europe in an exclusive duopoly between the Spanish and the Portuguese empires along a north-south meridian 370 leagues west of the Cape Verde islands (off the west coast of Africa), roughly 46° 36' W. (This boundary was known as the Line of Demarcation.)  The lands to the east would belong to Portugal and the lands to the west to Spain.", 'countries': ['Tordesillas', 'Portugal'], 'sentiment': 0.0}, {'year': 1498, 'description': '1498: Vasco da Gama sets foot on Kozhikode, starting the Portuguese presence in India', 'countries': ['India'], 'sentiment': 0.0}, {'year': 1500, 'description': '1500: Pedro Álvares Cabral sails to Brazil for the Portuguese king', 'countries': ['Brazil'], 'sentiment': 0.0}, {'year': 1511, 'description': '1511: The Portuguese capture Malacca, in present-day Malaysia', 'countries': ['Malaysia'], 'sentiment': 0.0}, {'year': 1515, 'description': '1515: Spanish Leyes de Burgos on January 25', 'countries': ['Leyes de Burgos'], 'sentiment': 0.0}, {'year': 1519, 'description': '1519: The Portuguese capture Ormus, in the Strait of Hormuz, in the Persian Gulf', 'countries': ['Ormus'], 'sentiment': 0.0}, {'year': 1542, 'description': '1542: Spanish Leyes Nuevas ("New Laws")', 'countries': [], 'sentiment': 0.0}, {'year': 1542, 'description': '1542: Creation of the Viceroyalty of Peru', 'countries': [], 'sentiment': 0.0}, {'year': 1550, 'description': '1550–1552: Valladolid Controversy and publication of A Short Account of the Destruction of the Indies by Bishop of Chiapas Bartolomé de las Casas[1]', 'countries': ['Valladolid'], 'sentiment': 0.0}, {'year': 1600, 'description': '1600: Queen Elizabeth I of England grants a Royal charter to the English East India Company', 'countries': ['England'], 'sentiment': 0.0}, {'year': 1602, 'description': '1602: Establishment of the Dutch East India Company', 'countries': [], 'sentiment': 0.0}, {'year': 1607, 'description': '1607: The first permanent English settlement in North America at Jamestown, Virginia', 'countries': ['North America', 'Jamestown', 'Virginia'], 'sentiment': 0.0}, {'year': 1612, 'description': '1612-1615: The Portuguese captured Gamru Port and a few other places (like Hormuz Island ) in southern coast of Iran.', 'countries': ['Iran'], 'sentiment': 0.0}, {'year': 1615, 'description': '1615–1622: Abbas I, king of Iran, battled the Portuguese with the aid of the Royal Navy and the English East India Company and recaptured those lands.', 'countries': ['Iran'], 'sentiment': 0.0}, {'year': 1619, 'description': '1619: The first African slaves arrive in Jamestown, Virginia', 'countries': ['Jamestown', 'Virginia'], 'sentiment': 0.0}, {'year': 1624, 'description': '1624: The English set foot in Surat', 'countries': ['Surat'], 'sentiment': 0.0}, {'year': 1625, 'description': '1625: Charles I of England receives Oldman, king of the Miskito Nation, who was taken to England by the Earl of Warwick.', 'countries': ['England'], 'sentiment': 0.0}, {'year': 1630, 'description': '1630: Puritans establish Massachusetts Bay Colony', 'countries': ['Puritans'], 'sentiment': 0.0}, {'year': 1717, 'description': '1717: Creation of the Viceroyalty of New Granada', 'countries': ['New Granada'], 'sentiment': 0.0}, {'year': 1775, 'description': '1775-1783: American War of Independence', 'countries': [], 'sentiment': 0.0}, {'year': 1776, 'description': '1776: Creation of the Viceroyalty of the Río de la Plata', 'countries': [], 'sentiment': 0.0}, {'year': 1776, 'description': '1776: The thirteen original colonies of the United States declare independence from Britain', 'countries': ['United States', 'Britain'], 'sentiment': 0.0}, {'year': 1784, 'description': "1784: Britain passes Pitt's India Act", 'countries': ['Britain'], 'sentiment': 0.0}, {'year': 1787, 'description': '1787: Britain creates Sierra Leone.', 'countries': ['Britain'], 'sentiment': 0.0}, {'year': 1788, 'description': '1788: Britain claims and proceeds to settle the eastern half of the continent of Australia.', 'countries': ['Britain', 'Australia'], 'sentiment': 0.0}, {'year': 1791, 'description': '1791-1804: Haitian Revolution and abolition of slavery by the French First Republic (reestablished by Napoleon in 1804)', 'countries': [], 'sentiment': 0.0}, {'year': 1795, 'description': '1795: Britain invades the Cape region of present-day South Africa', 'countries': ['Britain', 'South Africa'], 'sentiment': 0.0}, {'year': 1798, 'description': '1798: French Invasion of Egypt', 'countries': ['Egypt'], 'sentiment': -0.301688}, {'year': 1804, 'description': '1804–1813: Uprising in Serbia against the presence of the Ottoman Empire', 'countries': ['Serbia'], 'sentiment': 0.0}, {'year': 1810, 'description': '1810–1820s: Spanish American wars of independence', 'countries': [], 'sentiment': 0.0}, {'year': 1810, 'description': '1810–1821: Mexican War of Independence', 'countries': [], 'sentiment': 0.0}, {'year': 1815, 'description': '1815–1817: Serbian uprising leading to Serbian autonomy', 'countries': [], 'sentiment': 0.0}, {'year': 1820, 'description': '1820: The American Colonization Society (private citizens in the United States) created Liberia', 'countries': ['United States', 'Liberia'], 'sentiment': 0.0}, {'year': 1821, 'description': '1821–1823: Greek War of Independence', 'countries': [], 'sentiment': -0.378331}, {'year': 1822, 'description': '1822: Independence of Brazil proclaimed by Dom Pedro I', 'countries': ['Brazil'], 'sentiment': 0.0}, {'year': 1830, 'description': '1830: Start of the French conquest of Algeria', 'countries': ['Algeria'], 'sentiment': 0.0}, {'year': 1833, 'description': '1833: British abolish slavery in the West Indies; The owners are reimbursed.', 'countries': ['West Indies'], 'sentiment': 0.0}, {'year': 1834, 'description': "1834: Beginning of the Boers' Great Trek", 'countries': [], 'sentiment': 0.0}, {'year': 1839, 'description': '1839: Papal Encyclical In Supremo Apostolatus, condemning the slave trade', 'countries': [], 'sentiment': 0.0}, {'year': 1839, 'description': '1839–1842: First Opium War and First Anglo-Afghan War', 'countries': [], 'sentiment': -0.627522}, {'year': 1846, 'description': '1846–1848: Mexican–American War, which results in the Mexican Cession', 'countries': [], 'sentiment': 0.0}, {'year': 1848, 'description': '1848: Decree-law Victor Schoelcher which abolish slavery (permanently) in the French colonial empire', 'countries': [], 'sentiment': 0.0}, {'year': 1853, 'description': "1853–1855: Publication of Gobineau's An Essay on the Inequality of the Human Races (one of the first, major formulation of racial theories[2])", 'countries': [], 'sentiment': 0.0}, {'year': 1856, 'description': '1856–1860: Second Opium War', 'countries': [], 'sentiment': -0.611541}, {'year': 1857, 'description': '1857: Uprising in India against British occupation, which leads to the creation of the British Raj', 'countries': ['India'], 'sentiment': 0.0}, {'year': 1861, 'description': '1861–1867: French intervention in Mexico ordered by Napoleon III', 'countries': ['Mexico'], 'sentiment': 0.0}, {'year': 1870, 'description': '1870: Franco-Prussian War', 'countries': [], 'sentiment': 0.0}, {'year': 1870, 'description': '1870–1880s: Conquest of the Desert in Argentina, led by Julio Argentino Roca', 'countries': ['Argentina', 'Julio Argentino Roca'], 'sentiment': 0.0}, {'year': 1877, 'description': '1877–1878: War between Russia and the Ottoman Empire and March 3, 1878 Treaty of San Stefano', 'countries': ['Russia', 'San Stefano'], 'sentiment': 0.0}, {'year': 1878, 'description': '1878: Treaty of Berlin recognising the independence of Romania, Serbia and Montenegro and the autonomy of Bulgaria', 'countries': ['Romania', 'Serbia', 'Bulgaria'], 'sentiment': 0.0}, {'year': 1878, 'description': '1878–1881: Second Anglo-Afghan War', 'countries': [], 'sentiment': -0.296477}, {'year': 1879, 'description': '1879: Anglo-Zulu War', 'countries': ['Anglo-Zulu'], 'sentiment': 0.0}, {'year': 1880, 'description': '1880–81: First Boer War', 'countries': [], 'sentiment': 0.0}, {'year': 1883, 'description': '1883: Publication of The Story of an African Farm by Olive Schreiner', 'countries': [], 'sentiment': 0.0}, {'year': 1884, 'description': '1884–85: Berlin Conference (UK, France, Germany) which sets the right of conquest for the scramble for Africa', 'countries': ['UK', 'France', 'Germany'], 'sentiment': 0.0}, {'year': 1885, 'description': '1885: Foundation of the Indian National Congress', 'countries': [], 'sentiment': 0.0}, {'year': 1885, 'description': "1885: Treaty of Simulambuco (between Portugal and the N'Goyo Kingdom).", 'countries': ['Simulambuco', 'Portugal'], 'sentiment': 0.0}, {'year': 1887, 'description': '1887: France creates the Indochinese Union', 'countries': ['France'], 'sentiment': 0.0}, {'year': 1888, 'description': '1888: Lei Áurea ("Golden Law") on May 13 in Brazil which abolish slavery', 'countries': ['Brazil'], 'sentiment': 0.0}, {'year': 1889, 'description': '1889: Foundation of the Republic of Brazil', 'countries': [], 'sentiment': 0.0}, {'year': 1889, 'description': '1889: British South Africa Company of Cecil Rhodes chartered by the British government to seek treaties and administer territory between the Limpopo River and African Great Lakes.', 'countries': [], 'sentiment': 0.0}, {'year': 1890, 'description': '1890: Cecil Rhodes sends the Pioneer Column into Mashonaland, starting the process of annexing the territory which became Southern Rhodesia', 'countries': [], 'sentiment': 0.0}, {'year': 1891, 'description': '1891: The Stairs Expedition to Katanga kills its king, Msiri and obtains treaties from his successors for the territory to become the possession of Leopold II of Belgium', 'countries': ['Katanga'], 'sentiment': 0.0}, {'year': 1895, 'description': '1895: Treaty of Shimonoseki between Japan and China and Triple Intervention', 'countries': ['Shimonoseki', 'Japan', 'China'], 'sentiment': 0.0}, {'year': 1895, 'description': '1895: Creation of French West Africa (AOF)', 'countries': ['West Africa'], 'sentiment': 0.0}, {'year': 1895, 'description': '1895–1896: First Italo–Ethiopian War', 'countries': [], 'sentiment': 0.0}, {'year': 1896, 'description': '1896: Anglo-Zanzibar War (on August 27)', 'countries': [], 'sentiment': 0.0}, {'year': 1897, 'description': '1897: Punitive Expedition led by British Admiral Harry Rawson against Benin, which brings to an end the highly sophisticated West African Kingdom of Benin', 'countries': ['Benin'], 'sentiment': 0.0}, {'year': 1898, 'description': '1898: Fashoda Incident', 'countries': [], 'sentiment': 0.0}, {'year': 1898, 'description': '1898: Spanish–American War. United States defeated Spain and seizes Cuba, Puerto Rico, and the Philippines.', 'countries': ['Puerto Rico', 'United States', 'Cuba'], 'sentiment': 0.0}, {'year': 1899, 'description': "1899: Publication of Rudyard Kipling's The White Man's Burden, as well as Joseph Conrad's Heart of Darkness[3]", 'countries': [], 'sentiment': 0.0}, {'year': 1899, 'description': '1899–1902: Second Boer War', 'countries': [], 'sentiment': 0.0}, {'year': 1899, 'description': '1899–1913: Philippine–American War', 'countries': ['Phillipines'], 'sentiment': -0.329697}, {'year': 1902, 'description': "1902: Anglo-Japanese Alliance: end of Britain's Splendid isolation", 'countries': ['Britain'], 'sentiment': -0.397295}, {'year': 1904, 'description': '1904–05: Russo-Japanese War won by Japan', 'countries': ['Japan'], 'sentiment': -0.340919}, {'year': 1905, 'description': '1905: Partition of Bengal', 'countries': ['Bengal'], 'sentiment': 0.0}, {'year': 1905, 'description': '1905: First Moroccan Crisis after the March 31, 1905 visit of Kaiser Wilhelm to Tangiers', 'countries': ['Tangiers'], 'sentiment': 0.0}, {'year': 1906, 'description': '1906: Algeciras Conference to mediate the Tangier Crisis between France and Germany', 'countries': ['France', 'Tangier', 'Germany'], 'sentiment': 0.0}, {'year': 1910, 'description': '1910: Creation of French Equatorial Africa (AEF)', 'countries': [], 'sentiment': 0.0}, {'year': 1911, 'description': '1911: Chinese Revolution', 'countries': [], 'sentiment': 0.0}, {'year': 1912, 'description': '1912: France establish a full protectorate over Morocco', 'countries': ['France', 'Morocco'], 'sentiment': 0.0}, {'year': 1912, 'description': '1912–1913: Italo-Turkish War (Tripolitania and Cyrenaica are transferred from the Ottoman Empire to Italy)', 'countries': ['Italy'], 'sentiment': 0.0}, {'year': 1914, 'description': '1914–1918: World War I', 'countries': [], 'sentiment': -0.446712}, {'year': 1916, 'description': '1916: May 16 Sykes-Picot Agreement', 'countries': [], 'sentiment': 0.0}, {'year': 1916, 'description': '1916–1918: Arab Revolt initiated by Hussein bin Ali and Emir Faisal', 'countries': [], 'sentiment': 0.0}, {'year': 1918, 'description': "1918: Woodrow Wilson's January 9 speech on the Fourteen Points", 'countries': [], 'sentiment': 0.0}, {'year': 1919, 'description': "1919: Foundation of the League of Nations at the Paris Peace Conference and creation of the League of Nations Mandates (Iraq and Palestine — including Transjordan — are passed to Great Britain's control, Lebanon and Syria to France; the Cameroons and Togoland are split between the UK and France; Ruanda-Urundi goes to Belgium and Tanganyika to the UK; Nauru and New Guinea to Australia; the Trust Territory of the Pacific Islands and the South Pacific Mandate to Japan; Samoa to New Zealand and South West Africa to South Africa)", 'countries': ['Japan', 'New Guinea', 'Syria'], 'sentiment': 0.0}, {'year': 1919, 'description': '1919: Third Anglo-Afghan War', 'countries': [], 'sentiment': 0.0}, {'year': 1919, 'description': '1919: Non-Cooperation Movement led by Mahatma Gandhi', 'countries': [], 'sentiment': 0.0}, {'year': 1920, 'description': '1920: San Remo conference in April', 'countries': [], 'sentiment': 0.0}, {'year': 1920, 'description': '1920: Treaty of Sèvres on August 10 between the Triple Entente (UK, France and Russia) and the Ottoman Empire; Mustafa Kemal leads the Turkish War of Independence leading to the 1923 Treaty of Lausanne', 'countries': ['Sèvres', 'UK', 'France'], 'sentiment': 0.0}, {'year': 1922, 'description': '1922: Creation of the Soviet Union', 'countries': [], 'sentiment': 0.0}, {'year': 1923, 'description': '1923: Proclamation of the Republic of Turkey by Mustafa Kemal on October 29', 'countries': [], 'sentiment': 0.0}, {'year': 1924, 'description': '1924: British Empire Exhibition', 'countries': [], 'sentiment': 0.0}, {'year': 1925, 'description': '1925: Foundation of the Algerian Star of North Africa by Messali Hadj', 'countries': ['North Africa'], 'sentiment': 0.0}, {'year': 1921, 'description': '1921–1926: Rif War in Morocco, led by Abd el-Krim', 'countries': ['Morocco'], 'sentiment': 0.0}, {'year': 1927, 'description': '1927: May 19 Treaty of Jeddah accords independence to Saudi Arabia led by King Abdul Aziz', 'countries': ['Saudi Arabia'], 'sentiment': 0.0}, {'year': 1927, 'description': "1927–1928: Publication of André Gide's Voyage au Congo (Travels in the Congo).[4]", 'countries': ['Congo'], 'sentiment': 0.0}, {'year': 1931, 'description': '1931: Paris Colonial Exposition', 'countries': [], 'sentiment': 0.0}, {'year': 1931, 'description': '1931: Dominions of Australia, Canada, New Zealand, and South Africa gain independence from Britain', 'countries': ['Australia', 'Canada', 'New Zealand'], 'sentiment': 0.0}, {'year': 1932, 'description': '1932: Independence of Iraq', 'countries': ['Iraq'], 'sentiment': 0.0}, {'year': 1933, 'description': '1933: Publication of Gilberto Freyre\'s Casa-Grande & Senzala ("The Great House and the Slave Quarters" - 1933[5])', 'countries': [], 'sentiment': 0.0}, {'year': 1935, 'description': '1935: Aimé Césaire coins the word Négritude', 'countries': [], 'sentiment': 0.0}, {'year': 1936, 'description': '1936: Franco-Syrian Treaty of Independence (never ratified by France)', 'countries': ['France'], 'sentiment': 0.0}, {'year': 1936, 'description': '1936–1939: Great Arab Revolt in the British Mandate of Palestine', 'countries': [], 'sentiment': 0.0}, {'year': 1935, 'description': '1935–36: Second Italo-Abyssinian War', 'countries': [], 'sentiment': -0.296477}, {'year': 1941, 'description': '1941: Atlantic charter Endorsed by all the Allies of World War II; Calls for self-determination', 'countries': [], 'sentiment': 0.0}, {'year': 1941, 'description': '1941: Foundation of the Viet Minh by Ho Chi Minh', 'countries': [], 'sentiment': 0.0}, {'year': 1941, 'description': '1941: Syria proclaims its independence from Vichy France, which is recognized in 1944', 'countries': ['Syria'], 'sentiment': 0.0}, {'year': 1942, 'description': '1942: Quit India Movement called for by Gandhi on August 9', 'countries': [], 'sentiment': 0.0}, {'year': 1943, 'description': '1943: Independence of Lebanon', 'countries': ['Lebanon'], 'sentiment': 0.0}, {'year': 1944, 'description': '1944: Nelson Mandela joins the African National Congress', 'countries': [], 'sentiment': 0.0}, {'year': 1945, 'description': '1945:Allies of World War II form the United Nations in San Francisco', 'countries': ['San Francisco'], 'sentiment': 0.0}, {'year': 1945, 'description': '1945: Sétif massacre in Algeria on May 8', 'countries': ['Algeria'], 'sentiment': -0.307402}, {'year': 1945, 'description': '1945: Proclamation of the independence of Indonesia by Soekarno & Mohammad Hatta', 'countries': ['Indonesia'], 'sentiment': 0.0}, {'year': 1945, 'description': '1945: Proclamation of the independence of Vietnam by Ho Chi Minh', 'countries': ['Vietnam'], 'sentiment': 0.0}, {'year': 1945, 'description': '1945: Foundation of the Arab League on March 22 (Egypt, Iraq, Jordan, Lebanon, Saudi Arabia, Syria and Yemen)', 'countries': ['Egypt', 'Iraq'], 'sentiment': 0.0}, {'year': 1945, 'description': '1945: Fifty states sign the Charter of the United Nations on June 26', 'countries': [], 'sentiment': 0.0}, {'year': 1945, 'description': '1945–1950: Chinese Civil War between the nationalist Kuomintang and the Communist Party led by Mao Zedong', 'countries': [], 'sentiment': 0.0}, {'year': 1946, 'description': '1946–1954: First Indochina War', 'countries': ['Indochina'], 'sentiment': 0.0}, {'year': 1947, 'description': '1947: Official start of the Cold War (see Cold War (1947-1953) and Cold War (1953-1962))', 'countries': [], 'sentiment': -0.33581}, {'year': 1947, 'description': '1947: Independence of India and of Pakistan (Pakistan came into being on August 14, and India on August 15)[6]', 'countries': ['India', 'Pakistan'], 'sentiment': 0.0}, {'year': 1947, 'description': '1947: UN Resolution 181 on the partition of Palestine in favor of a Two-state solution.', 'countries': ['Palestine'], 'sentiment': 0.0}, {'year': 1947, 'description': '1947: French repression of the Malagasy uprising. 90 to 100 000 killed.', 'countries': [], 'sentiment': -0.566204}, {'year': 1948, 'description': '1948: Declaration of the establishment of the State of Israel on May 14 and first Arab-Israeli War', 'countries': ['Israel'], 'sentiment': -0.392185}, {'year': 1948, 'description': '1948: Colonial exhibition in Belgium', 'countries': ['Belgium'], 'sentiment': 0.0}, {'year': 1949, 'description': "1949: Proclamation of the People's Republic of China by Mao Zedong", 'countries': ['China'], 'sentiment': 0.0}, {'year': 1951, 'description': "1951: Publication of Hannah Arendt's The Origins of Totalitarianism (second section dedicated to imperialism)", 'countries': [], 'sentiment': 0.0}, {'year': 1952, 'description': '1952: Alfred Sauvy coins the term "Third World"', 'countries': [], 'sentiment': 0.0}, {'year': 1954, 'description': '1954: French establishments in India cease to exist after de facto transfer to the Indian Union (de jure union accomplished in 1962)', 'countries': ['India'], 'sentiment': 0.0}, {'year': 1954, 'description': '1954: Battle of Dien Bien Phu & 1954 Geneva Accords marks the end of French Indochina', 'countries': [], 'sentiment': 0.0}, {'year': 1955, 'description': '1955: Bandung Conference', 'countries': [], 'sentiment': 0.0}, {'year': 1956, 'description': "1956: Suez Crisis between Israel, the UK and France against Egypt, after Nasser's nationalisation of the Suez Canal Company", 'countries': ['Israel', 'UK', 'Egypt'], 'sentiment': 0.0}, {'year': 1957, 'description': "1957: Algerian independence militant Larbi Ben M'Hidi murdered in prison, early March", 'countries': [], 'sentiment': -0.6071}, {'year': 1957, 'description': '1957: First country sub-Saharan Africa (Ghana) regains independence.', 'countries': ['Ghana', 'sub-Saharan Africa'], 'sentiment': 0.0}, {'year': 1958, 'description': '1958: Foundation of the United Arab Republic as a first step toward a Pan-Arab nation; it is formed by Egypt and Syria (until 1961). Creation also of the short-term Arab Federation of Iraq and Jordan.', 'countries': ['United Arab Republic', 'Syria'], 'sentiment': 0.0}, {'year': 1959, 'description': '1959: Independence of Morocco and Tunisia', 'countries': ['Morocco', 'Tunisia'], 'sentiment': 0.0}, {'year': 1960, 'description': '1960: Independence of French colonies in Africa; the UN reach 99 members states', 'countries': ['Africa'], 'sentiment': 0.0}, {'year': 1961, 'description': '1961: Assassination of Patrice Lumumba, first prime minister of the Democratic Republic of the Congo, on January 17', 'countries': [], 'sentiment': 0.0}, {'year': 1961, 'description': '1961: Formation of the Conferência das Organizações Nacionalistas das Colónias Portuguesas on April 18 in Casablanca, Morocco (PAIGC, MPLA, FRELIMO and MLSTP)', 'countries': ['Casablanca', 'Morocco'], 'sentiment': 0.0}, {'year': 1961, 'description': '1961: Creation of the Non-Aligned Movement', 'countries': [], 'sentiment': 0.0}, {'year': 1961, 'description': '1961: Soviet premier Khrushchev declares that the Soviet Union would support all "national liberation movements"', 'countries': [], 'sentiment': 0.0}, {'year': 1961, 'description': "1961: Publication of Frantz Fanon' The Wretched of the Earth", 'countries': [], 'sentiment': -0.643158}, {'year': 1961, 'description': '1961: October 17 Paris massacre', 'countries': ['Paris'], 'sentiment': 0.0}, {'year': 1961, 'description': '1961: Indian annexation of Goa ends Portuguese India (Goa, Dadra, Nagar Haveli, Daman and Diu).', 'countries': ['Goa', 'India'], 'sentiment': 0.0}, {'year': 1961, 'description': '1961–1974: Portuguese Colonial War; See also Angolan War of Independence (1961-1989)', 'countries': [], 'sentiment': 0.0}, {'year': 1962, 'description': '1962: Évian Accords halts the Algerian War and puts end to French rule in North-Africa', 'countries': ['North-Africa'], 'sentiment': 0.0}, {'year': 1963, 'description': '1963: Assassination of Sylvanus Olympio on January 13, first president of Togo; he is replaced by Gnassingbé Eyadéma, who ruled over Togo until his death in 2005', 'countries': ['Togo'], 'sentiment': 0.0}, {'year': 1965, 'description': '1965–1975: Vietnam War', 'countries': ['Vietnam'], 'sentiment': 0.0}, {'year': 1965, 'description': '1965: Assassination of Mehdi Ben Barka, leader of the UNPF and of the Tricontinental Conference', 'countries': [], 'sentiment': 0.0}, {'year': 1965, 'description': '1965: Joseph Mobutu becomes the dictator of the Democratic Republic of Congo until his overthrow in 1997 by Laurent-Désiré Kabila', 'countries': ['Democratic Republic of Congo'], 'sentiment': 0.0}, {'year': 1967, 'description': '1967: Assassination of Che Guevara in Bolivia.', 'countries': ['Bolivia'], 'sentiment': 0.0}, {'year': 1969, 'description': '1969: Assassination of Eduardo Mondlane, leader of the FRELIMO', 'countries': [], 'sentiment': 0.0}, {'year': 1970, 'description': '1970s: Independence of the former Portuguese colonies, following the April 25, 1974 Carnation Revolution and the Portuguese Colonial War', 'countries': [], 'sentiment': 0.0}, {'year': 1971, 'description': '1971: Independence of Bangladesh following the war with Pakistan', 'countries': ['Bangladesh', 'Pakistan'], 'sentiment': 0.0}, {'year': 1971, 'description': "1971: Publication of Eduardo Galeano's Open Veins of Latin America[7]", 'countries': [], 'sentiment': 0.0}, {'year': 1971, 'description': "1971: Publication of Gustavo Gutiérrez's A Theology of Liberation: History, Politics, Salvation[8]", 'countries': [], 'sentiment': 0.0}, {'year': 1973, 'description': '1973: Assassination of Amilcar Cabral, leader of the African Party for the Independence of Guinea and Cape Verde (PAIGC) on January 20', 'countries': [], 'sentiment': 0.0}, {'year': 1973, 'description': '1973: The PAIGC proclaims the independence of Guinea-Bissau on September 24', 'countries': ['Guinea-Bissau'], 'sentiment': 0.0}, {'year': 1975, 'description': "1975: Portugal recognizes Mozambique's independence on June 25 and Angola on November 11", 'countries': ['Portugal', 'Mozambique', 'Angola'], 'sentiment': 0.0}, {'year': 1979, 'description': '1979: Soviet invasion of Afghanistan and start of the "Second Cold War"', 'countries': ['Afghanistan'], 'sentiment': 0.0}, {'year': 1980, 'description': '1980: The UN reaches 154 member states', 'countries': [], 'sentiment': 0.0}, {'year': 1980, 'description': '1980: Assassination of Óscar Romero, prelate archbishop of San Salvador and proponent of the Liberation theology, on March 24', 'countries': ['San Salvador'], 'sentiment': 0.0}, {'year': 1982, 'description': '1982: Latin American debt crisis (in particular in Mexico, Brazil and Argentina)', 'countries': ['Mexico', 'Brazil', 'Argentina'], 'sentiment': -0.369229}, {'year': 1988, 'description': '1988: Assassination of Dulcie September, member of the African National Congress', 'countries': [], 'sentiment': 0.0}, {'year': 1989, 'description': '1989: Operation Just Cause against Manuel Noriega', 'countries': [], 'sentiment': -0.293424}, {'year': 1990, 'description': '1990: Independence of Namibia, the UN reaches 159 states.', 'countries': ['Namibia'], 'sentiment': 0.0}, {'year': 1994, 'description': "1994: Nelson Mandela becomes president of South Africa in the nation's first all race election", 'countries': ['South Africa'], 'sentiment': 0.0}, {'year': 2001, 'description': '2001: French law recognizing slavery and the Atlantic slave trade as crimes against humanity (Taubira Law)', 'countries': [], 'sentiment': -0.552231}, {'year': 2005, 'description': '2005: February 23 French law on the "positive aspects" of "French presence abroad, in particular in North Africa"', 'countries': ['North Africa'], 'sentiment': 0.0}, {'year': 2006, 'description': '2006: Repeal of the February 23, 2005 French law, following criticisms of historical revisionism', 'countries': [], 'sentiment': 0.0}, {'year': 2010, 'description': '2010: Dissolution of the Netherlands Antilles', 'countries': ['Netherlands'], 'sentiment': 0.0}]

data_n = data[:]
for i in data_n:
    for j in range(len(i['countries'])):
        if i['countries'][j] in my_dict2.keys():
            j_clone = i['countries'][j][:]
            i['countries'][j] = my_dict2[j_clone]
    for i in data_n:
        if 'independence' in i['description'] or 'positive' in i['description']:
            i['sentiment'] = 'green'
        if i['sentiment'] == None or i['sentiment'] == 0.0:
                i['sentiment'] = None
    for i in data_n:
        y_clone = i['year']
        i['year'] = abs(y_clone - 1492) * 2

print(data_n)
# with open('data.json', 'w') as outfile:
#      json.dump(data_n, outfile)