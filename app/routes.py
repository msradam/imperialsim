from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InputForm
import json 
from app.model_run import *

dataset = [{
  'year': 2984,
  'description': '1492: "Discovery" of the "New World" and symbolic date of the European Age of Exploration; beginning of the colonization of the Americas and of the Columbian Exchange',
  'countries': ['US'],
  'sentiment': '#EC2049'
}, {
  'year': 2824,
  'description': '1493: Papal Bull Inter caetera on May 4',
  'countries': ['CV'],
  'sentiment': '#EC2049'
}, {
  'year': 2664,
  'description': "1494: Treaty of Tordesillas dividing the world outside of Europe in an exclusive duopoly between the Spanish and the Portuguese empires along a north-south meridian 370 leagues west of the Cape Verde islands (off the west coast of Africa), roughly 46° 36' W. (This boundary was known as the Line of Demarcation.)  The lands to the east would belong to Portugal and the lands to the west to Spain.",
  'countries': ['PT'],
  'sentiment': '#EC2049'
}, {
  'year': 2024,
  'description': '1498: Vasco da Gama sets foot on Kozhikode, starting the Portuguese presence in India',
  'countries': ['IN'],
  'sentiment': '#EC2049'
}, {
  'year': 1704,
  'description': '1500: Pedro Álvares Cabral sails to Brazil for the Portuguese king',
  'countries': ['BR'],
  'sentiment': '#F26B38'
}, {
  'year': 56,
  'description': '1511: The Portuguese capture Malacca, in present-day Malaysia',
  'countries': ['MY'],
  'sentiment': '#EC2049'
}, {
  'year': 696,
  'description': '1515: Spanish Leyes de Burgos on January 25',
  'countries': ['US'],
  'sentiment': '#EC2049'
}, {
  'year': 1336,
  'description': '1519: The Portuguese capture Ormus, in the Strait of Hormuz, in the Persian Gulf',
  'countries': ['IR'],
  'sentiment': '#EC2049'
}, {
  'year': 952,
  'description': '1542: Spanish Leyes Nuevas ("New Laws")',
  'countries': ['US'],
  'sentiment': '#EC2049'
}, {
  'year': 952,
  'description': '1542: Creation of the Viceroyalty of Peru',
  'countries': ['PE'],
  'sentiment': '#F26B38'
}, {
  'year': 328,
  'description': '1550–1552: Valladolid Controversy and publication of A Short Account of the Destruction of the Indies by Bishop of Chiapas Bartolomé de las Casas[1]',
  'countries': ['GY'],
  'sentiment': '#2F9599 '
}, {
  'year': 2360,
  'description': '1600: Queen Elizabeth I of England grants a Royal charter to the English East India Company',
  'countries': ['IN'],
  'sentiment': '#EC2049'
}, {
  'year': 2680,
  'description': '1602: Establishment of the Dutch East India Company',
  'countries': ['GB'],
  'sentiment': '#2F9599 '
}, {
  'year': 2488,
  'description': '1607: The first permanent English settlement in North America at Jamestown, Virginia',
  'countries': ['US'],
  'sentiment': '#EC2049'
}, {
  'year': 1688,
  'description': '1612-1615: The Portuguese captu#EC2049 Gamru Port and a few other places (like Hormuz Island ) in southern coast of Iran.',
  'countries': ['IR'],
  'sentiment': '#EC2049'
}, {
  'year': 1208,
  'description': '1615–1622: Abbas I, king of Iran, battled the Portuguese with the aid of the Royal Navy and the English East India Company and recaptu#EC2049 those lands.',
  'countries': ['IR'],
  'sentiment': '#2F9599 '
}, {
  'year': 568,
  'description': '1619: The first African slaves arrive in Jamestown, Virginia',
  'countries': ['US'],
  'sentiment': '#EC2049'
}, {
  'year': 232,
  'description': '1624: The English set foot in Surat',
  'countries': ['IN'],
  'sentiment': '#F26B38'
}, {
  'year': 392,
  'description': '1625: Charles I of England receives Oldman, king of the Miskito Nation, who was taken to England by the Earl of Warwick.',
  'countries': ['England'],
  'sentiment': None
}, {
  'year': 1192,
  'description': '1630: Puritans establish Massachusetts Bay Colony',
  'countries': ['US'],
  'sentiment': '#F26B38'
}, {
  'year': 2792,
  'description': '1717: Creation of the Viceroyalty of New Granada',
  'countries': ['CO'],
  'sentiment': '#F26B38'
}, {
  'year': 520,
  'description': '1775-1783: American War of Independence',
  'countries': ['US'],
  'sentiment': '#2F9599 '
}, {
  'year': 680,
  'description': '1776: Creation of the Viceroyalty of the Río de la Plata',
  'countries': ['EC'],
  'sentiment': '#F26B38'
}, {
  'year': 680,
  'description': '1776: The thirteen original colonies of the United States declare independence from Britain',
  'countries': ['US'],
  'sentiment': '#2F9599 '
}, {
  'year': 1960,
  'description': "1784: Britain passes Pitt's India Act",
  'countries': ['IN'],
  'sentiment': '#EC2049'
}, {
  'year': 2440,
  'description': '1787: Britain creates Sierra Leone.',
  'countries': ['SL'],
  'sentiment': '#EC2049'
}, {
  'year': 2600,
  'description': '1788: Britain claims and proceeds to settle the eastern half of the continent of Australia.',
  'countries': ['AU'],
  'sentiment': '#EC2049'
}, {
  'year': 2888,
  'description': '1791-1804: Haitian Revolution and abolition of slavery by the French First Republic (reestablished by Napoleon in 1804)',
  'countries': ['HT'],
  'sentiment': '#2F9599 '
}, {
  'year': 2248,
  'description': '1795: Britain invades the Cape region of present-day South Africa',
  'countries': ['ZA'],
  'sentiment': '#EC2049'
}, {
  'year': 1768,
  'description': '1798: French Invasion of Egypt',
  'countries': ['EG'],
  'sentiment': '#EC2049'
}, {
  'year': 808,
  'description': '1804–1813: Uprising in Serbia against the presence of the Ottoman Empire',
  'countries': ['RS'],
  'sentiment': '#2F9599 '
}, {
  'year': 152,
  'description': '1810–1820s: Spanish American wars of independence',
  'countries': ['MX'],
  'sentiment': '#2F9599 '
}, {
  'year': 152,
  'description': '1810–1821: Mexican War of Independence',
  'countries': ['MX'],
  'sentiment': '#2F9599 '
}, {
  'year': 952,
  'description': '1815–1817: Serbian uprising leading to Serbian autonomy',
  'countries': ['RS'],
  'sentiment': '#2F9599 '
}, {
  'year': 1752,
  'description': '1820: The American Colonization Society (private citizens in the United States) created Liberia',
  'countries': ['LR'],
  'sentiment': '#F26B38'
}, {
  'year': 1912,
  'description': '1821–1823: Greek War of Independence',
  'countries': ['GR'],
  'sentiment': '#2F9599 '
}, {
  'year': 2072,
  'description': '1822: Independence of Brazil proclaimed by Dom Pedro LI',
  'countries': ['BR'],
  'sentiment': '#2F9599 '
}, {
  'year': 2616,
  'description': '1830: Start of the French conquest of Algeria',
  'countries': ['DZ'],
  'sentiment': '#EC2049'
}, {
  'year': 2136,
  'description': '1833: British abolish slavery in the West Indies; The owners are reimbursed.',
  'countries': ['GY'],
  'sentiment': '#2F9599 '
}, {
  'year': 1976,
  'description': "1834: Beginning of the Boers' Great Trek",
  'countries': ['ZA'],
  'sentiment': '#F26B38'
}, {
  'year': 1176,
  'description': '1839: Papal Encyclical In Supremo Apostolatus, condemning the slave trade',
  'countries': [],
  'sentiment': '#2F9599 '
}, {
  'year': 1176,
  'description': '1839–1842: First Opium War and First Anglo-Afghan War',
  'countries': ['AF'],
  'sentiment': '#F26B38'
}, {
  'year': 56,
  'description': '1846–1848: Mexican–American War, which results in the Mexican Cession',
  'countries': ['MX'],
  'sentiment': '#2F9599 '
}, {
  'year': 264,
  'description': '1848: Decree-law Victor Schoelcher which abolish slavery (permanently) in the French colonial empire',
  'countries': [],
  'sentiment': None
}, {
  'year': 1064,
  'description': "1853–1855: Publication of Gobineau's An Essay on the Inequality of the Human Races (one of the first, major formulation of racial theories[2])",
  'countries': [],
  'sentiment': None
}, {
  'year': 1544,
  'description': '1856–1860: Second Opium War',
  'countries': ['CN'],
  'sentiment': '#EC2049'
}, {
  'year': 1704,
  'description': '1857: Uprising in India against British occupation, which leads to the creation of the British Raj',
  'countries': ['IN'],
  'sentiment': '#F26B38'
}, {
  'year': 2344,
  'description': '1861–1867: French intervention in Mexico orde#EC2049 by Napoleon III',
  'countries': ['MX'],
  'sentiment': '#EC2049'
}, {
  'year': 2184,
  'description': '1870: Franco-Prussian War',
  'countries': ['DE'],
  'sentiment': '#F26B38'
}, {
  'year': 2184,
  'description': '1870–1880s: Conquest of the Desert in Argentina, led by Julio Argentino Roca',
  'countries': ['AR'],
  'sentiment': '#F26B38'
}, {
  'year': 1064,
  'description': '1877–1878: War between Russia and the Ottoman Empire and March 3, 1878 Treaty of San Stefano',
  'countries': ['IR'],
  'sentiment': '#F26B38'
}, {
  'year': 904,
  'description': '1878: Treaty of Berlin recognising the independence of Romania, Serbia and Montenegro and the autonomy of Bulgaria',
  'countries': ['RO'],
  'sentiment': '#2F9599 '
}, {
  'year': 904,
  'description': '1878: Treaty of Berlin recognising the independence of Romania, Serbia and Montenegro and the autonomy of Bulgaria',
  'countries': ['RS'],
  'sentiment': '#2F9599 '
}, {
  'year': 904,
  'description': '1878: Treaty of Berlin recognising the independence of Romania, Serbia and Montenegro and the autonomy of Bulgaria',
  'countries': ['BG'],
  'sentiment': '#2F9599 '
}, {
  'year': 904,
  'description': '1878–1881: Second Anglo-Afghan War',
  'countries': ['AF'],
  'sentiment': '#F26B38'
}, {
  'year': 744,
  'description': '1879: Anglo-Zulu War',
  'countries': ['ZA'],
  'sentiment': '#F26B38'
}, {
  'year': 584,
  'description': '1880–81: First Boer War',
  'countries': ['ZA'],
  'sentiment': '#2F9599 '
}, {
  'year': 104,
  'description': '1883: Publication of The Story of an African Farm by Olive Schreiner',
  'countries': ['ZA'],
  'sentiment': '#2F9599 '
}, {
  'year': 56,
  'description': '1884–85: Berlin Conference (UK, France, Germany) which sets the right of conquest for the scramble for Africa',
  'countries': ['FR'],
  'sentiment': '#EC2049'
}, {
  'year': 216,
  'description': '1885: Foundation of the Indian National Congress',
  'countries': ['IN'],
  'sentiment': '#2F9599 '
}, {
  'year': 216,
  'description': "1885: Treaty of Simulambuco (between Portugal and the N'Goyo Kingdom).",
  'countries': ['CG'],
  'sentiment': '#2F9599 '
}, {
  'year': 536,
  'description': '1887: France creates the Indochinese Union',
  'countries': ['IN'],
  'sentiment': '#EC2049'
}, {
  'year': 696,
  'description': '1888: Lei Áurea ("Golden Law") on May 13 in Brazil which abolish slavery',
  'countries': ['BR'],
  'sentiment': '#2F9599 '
}, {
  'year': 856,
  'description': '1889: Foundation of the Republic of Brazil',
  'countries': ['BR'],
  'sentiment': '#2F9599 '
}, {
  'year': 856,
  'description': '1889: British South Africa Company of Cecil Rhodes charte#EC2049 by the British government to seek treaties and administer territory between the Limpopo River and African Great Lakes.',
  'countries': ['MZ'],
  'sentiment': '#EC2049'
}, {
  'year': 1016,
  'description': '1890: Cecil Rhodes sends the Pioneer Column into Mashonaland, starting the process of annexing the territory which became Southern Rhodesia',
  'countries': ['ZW'],
  'sentiment': '#EC2049'
}, {
  'year': 1176,
  'description': '1891: The Stairs Expedition to Katanga kills its king, Msiri and obtains treaties from his successors for the territory to become the possession of Leopold II of Belgium',
  'countries': ['CG'],
  'sentiment': '#EC2049'
}, {
  'year': 1816,
  'description': '1895: Treaty of Shimonoseki between Japan and China and Triple Intervention',
  'countries': ['JP'],
  'sentiment': '#2F9599 '
}, {
  'year': 1816,
  'description': '1895: Creation of French West Africa (AOF)',
  'countries': ['SN'],
  'sentiment': '#EC2049'
}, {
  'year': 1816,
  'description': '1895–1896: First Italo–Ethiopian War',
  'countries': ['ET'],
  'sentiment': '#F26B38'
}, {
  'year': 1976,
  'description': '1896: Anglo-Zanzibar War (on August 27)',
  'countries': ['TZ'],
  'sentiment': '#F26B38'
}, {
  'year': 2136,
  'description': '1897: Punitive Expedition led by British Admiral Harry Rawson against Benin, which brings to an end the highly sophisticated West African Kingdom of Benin',
  'countries': ['BJ'],
  'sentiment': '#EC2049'
}, {
  'year': 2296,
  'description': '1898: Fashoda Incident',
  'countries': ['MA'],
  'sentiment': '#F26B38'
}, {
  'year': 2296,
  'description': '1898: Spanish–American War. United States defeated Spain and seizes Cuba, Puerto Rico, and the Philippines.',
  'countries': ['PR'],
  'sentiment': '#EC2049'
},{
  'year': 2296,
  'description': '1898: Spanish–American War. United States defeated Spain and seizes Cuba, Puerto Rico, and the Philippines.',
  'countries': ['CU'],
  'sentiment': '#EC2049'
}, {
  'year': 2456,
  'description': "1899: Publication of Rudyard Kipling's The White Man's Burden, as well as Joseph Conrad's Heart of Darkness[3]",
  'countries': ['IN'],
  'sentiment': '#F26B38'
}, {
  'year': 2456,
  'description': '1899–1902: Second Boer War',
  'countries': ['ZA'],
  'sentiment': '#F26B38'
}, {
  'year': 2456,
  'description': '1899–1913: Philippine–American War',
  'countries': ['PH'],
  'sentiment': '#F26B38'
}, {
  'year': 2936,
  'description': "1902: Anglo-Japanese Alliance: end of Britain's Splendid isolation",
  'countries': ['JP'],
  'sentiment': '#F26B38'
}, {
  'year': 2712,
  'description': '1904–05: Russo-Japanese War won by Japan',
  'countries': ['JP'],
  'sentiment': '#EC2049'
}, {
  'year': 2552,
  'description': '1905: Partition of Bengal',
  'countries': ['BD'],
  'sentiment': '#EC2049'
}, {
  'year': 2552,
  'description': '1905: First Moroccan Crisis after the March 31, 1905 visit of Kaiser Wilhelm to Tangiers',
  'countries': ['MA'],
  'sentiment': '#EC2049'
}, {
  'year': 2392,
  'description': '1906: Algeciras Conference to mediate the Tangier Crisis between France and Germany',
  'countries': ['MA'],
  'sentiment': '#F26B38'
}, {
  'year': 1752,
  'description': '1910: Creation of French Equatorial Africa (AEF)',
  'countries': ['TD'],
  'sentiment': '#EC2049'
}, {
  'year': 1592,
  'description': '1911: Chinese Revolution',
  'countries': ['CN'],
  'sentiment': '#F26B38'
}, {
  'year': 1432,
  'description': '1912: France establish a full protectorate over Morocco',
  'countries': ['MA'],
  'sentiment': '#EC2049'
}, {
  'year': 1432,
  'description': '1912–1913: Italo-Turkish War (Tripolitania and Cyrenaica are transfer#EC2049 from the Ottoman Empire to Italy)',
  'countries': ['TR'],
  'sentiment': '#EC2049'
}, {
  'year': 1112,
  'description': '1914–1918: World War I',
  'countries': [],
  'sentiment': '#EC2049'
}, {
  'year': 792,
  'description': '1916: May 16 Sykes-Picot Agreement',
  'countries': ['TR'],
  'sentiment': '#F26B38'
}, {
  'year': 792,
  'description': '1916–1918: Arab Revolt initiated by Hussein bin Ali and Emir Faisal',
  'countries': ['SA'],
  'sentiment': '#2F9599 '
}, {
  'year': 472,
  'description': "1918: Woodrow Wilson's January 9 speech on the Fourteen Points",
  'countries': [],
  'sentiment': None
}, {
  'year': 312,
  'description': "1919: Foundation of the League of Nations at the Paris Peace Conference and creation of the League of Nations Mandates (Iraq and Palestine — including Transjordan — are passed to Great Britain's control, Lebanon and Syria to France; the Cameroons and Togoland are split between the UK and France; Ruanda-Urundi goes to Belgium and Tanganyika to the UK; Nauru and New Guinea to Australia; the Trust Territory of the Pacific Islands and the South Pacific Mandate to Japan; Samoa to New Zealand and South West Africa to South Africa)",
  'countries': ['PG'],
  'sentiment': '#EC2049'
}, {
  'year': 312,
  'description': '1919: Third Anglo-Afghan War',
  'countries': ['AF'],
  'sentiment': '#F26B38'
}, {
  'year': 312,
  'description': '1919: Non-Cooperation Movement led by Mahatma Gandhi',
  'countries': ['IN'],
  'sentiment': '#EC2049'
}, {
  'year': 152,
  'description': '1920: San Remo conference in April',
  'countries': ['SY'],
  'sentiment': '#EC2049'
}, {
  'year': 152,
  'description': '1920: Treaty of Sèvres on August 10 between the Triple Entente (UK, France and Russia) and the Ottoman Empire; Mustafa Kemal leads the Turkish War of Independence leading to the 1923 Treaty of Lausanne',
  'countries': ['TR'],
  'sentiment': '#F26B38'
}, {
  'year': 168,
  'description': '1922: Creation of the Soviet Union',
  'countries': ['RU'],
  'sentiment': '#2F9599 '
}, {
  'year': 328,
  'description': '1923: Proclamation of the Republic of Turkey by Mustafa Kemal on October 29',
  'countries': ['TR"'],
  'sentiment': '#2F9599 '
}, {
  'year': 488,
  'description': '1924: British Empire Exhibition',
  'countries': ['GB'],
  'sentiment': '#2F9599 '
}, {
  'year': 648,
  'description': '1925: Foundation of the Algerian Star of North Africa by Messali Hadj',
  'countries': ['DZ'],
  'sentiment': '#2F9599 '
}, {
  'year': 8,
  'description': '1921–1926: Rif War in Morocco, led by Abd el-Krim',
  'countries': ['MA'],
  'sentiment': '#F26B38'
}, {
  'year': 968,
  'description': '1927: May 19 Treaty of Jeddah accords independence to Saudi Arabia led by King Abdul Aziz',
  'countries': ['SA'],
  'sentiment': '#2F9599 '
}, {
  'year': 968,
  'description': "1927–1928: Publication of André Gide's Voyage au Congo (Travels in the Congo).[4]",
  'countries': ['CG'],
  'sentiment': '#2F9599 '
}, {
  'year': 1608,
  'description': '1931: Paris Colonial Exposition',
  'countries': ['FR'],
  'sentiment': '#2F9599 '
}, {
  'year': 1608,
  'description': '1931: Dominions of Australia, Canada, New Zealand, and South Africa gain independence from Britain',
  'countries': ['AU'],
  'sentiment': '#2F9599 '
}, {
  'year': 1608,
  'description': '1931: Dominions of Australia, Canada, New Zealand, and South Africa gain independence from Britain',
  'countries': ['CA'],
  'sentiment': '#2F9599 '
}, {
  'year': 1608,
  'description': '1931: Dominions of Australia, Canada, New Zealand, and South Africa gain independence from Britain',
  'countries': ['NZ'],
  'sentiment': '#2F9599 '
}, {
  'year': 1768,
  'description': '1932: Independence of Iraq',
  'countries': ['IQ'],
  'sentiment': '#2F9599 '
}, {
  'year': 1928,
  'description': '1933: Publication of Gilberto Freyre\'s Casa-Grande & Senzala ("The Great House and the Slave Quarters" - 1933[5])',
  'countries': [],
  'sentiment': '#EC2049'
}, {
  'year': 2248,
  'description': '1935: Aimé Césaire coins the word Négritude',
  'countries': [],
  'sentiment': '#EC2049'
}, {
  'year': 2408,
  'description': '1936: Franco-Syrian Treaty of Independence (never ratified by France)',
  'countries': ['SY'],
  'sentiment': '#F26B38'
}, {
  'year': 2408,
  'description': '1936–1939: Great Arab Revolt in the British Mandate of Palestine',
  'countries': ['PS'],
  'sentiment': '#F26B38'
}, {
  'year': 2248,
  'description': '1935–36: Second Italo-Abyssinian War',
  'countries': ['ET'],
  'sentiment': '#F26B38'
}, {
  'year': 2760,
  'description': '1941: Atlantic charter Endorsed by all the Allies of World War II; Calls for self-determination',
  'countries': [],
  'sentiment': None
}, {
  'year': 2760,
  'description': '1941: Foundation of the Viet Minh by Ho Chi Minh',
  'countries': ['VN'],
  'sentiment': '#2F9599 '
}, {
  'year': 2760,
  'description': '1941: Syria proclaims its independence from Vichy France, which is recognized in 1944',
  'countries': ['SY'],
  'sentiment': '#2F9599 '
}, {
  'year': 2600,
  'description': '1942: Quit India Movement called for by Gandhi on August 9',
  'countries': ['IN'],
  'sentiment': '#2F9599 '
}, {
  'year': 2440,
  'description': '1943: Independence of Lebanon',
  'countries': ['LB'],
  'sentiment': '#2F9599 '
}, {
  'year': 2280,
  'description': '1944: Nelson Mandela joins the African National Congress',
  'countries': ['ZA'],
  'sentiment': '#2F9599 '
}, {
  'year': 2120,
  'description': '1945:Allies of World War II form the United Nations in San Francisco',
  'countries': ['US'],
  'sentiment': '#2F9599 '
}, {
  'year': 2120,
  'description': '1945: Sétif massacre in Algeria on May 8',
  'countries': ['DZ'],
  'sentiment': '#EC2049'
}, {
  'year': 2120,
  'description': '1945: Proclamation of the independence of Indonesia by Soekarno & Mohammad Hatta',
  'countries': ['ID'],
  'sentiment': '#2F9599 '
}, {
  'year': 2120,
  'description': '1945: Proclamation of the independence of Vietnam by Ho Chi Minh',
  'countries': ['VN'],
  'sentiment': '#2F9599 '
}, {
  'year': 2120,
  'description': '1945: Foundation of the Arab League on March 22 (Egypt, Iraq, Jordan, Lebanon, Saudi Arabia, Syria and Yemen)',
  'countries': ['EG'],
  'sentiment': None
}, {
  'year': 2120,
  'description': '1945: Foundation of the Arab League on March 22 (Egypt, Iraq, Jordan, Lebanon, Saudi Arabia, Syria and Yemen)',
  'countries': ['IQ'],
  'sentiment': '#2F9599 '
},{
  'year': 2120,
  'description': '1945: Foundation of the Arab League on March 22 (Egypt, Iraq, Jordan, Lebanon, Saudi Arabia, Syria and Yemen)',
  'countries': ['JO'],
  'sentiment': '#2F9599 '
},{
  'year': 2120,
  'description': '1945: Foundation of the Arab League on March 22 (Egypt, Iraq, Jordan, Lebanon, Saudi Arabia, Syria and Yemen)',
  'countries': ['LB'],
  'sentiment': '#2F9599 '
},{
  'year': 2120,
  'description': '1945: Foundation of the Arab League on March 22 (Egypt, Iraq, Jordan, Lebanon, Saudi Arabia, Syria and Yemen)',
  'countries': ['SA'],
  'sentiment': '#2F9599 '
},{
  'year': 2120,
  'description': '1945: Foundation of the Arab League on March 22 (Egypt, Iraq, Jordan, Lebanon, Saudi Arabia, Syria and Yemen)',
  'countries': ['SY'],
  'sentiment': '#2F9599 '
},{
  'year': 2120,
  'description': '1945: Foundation of the Arab League on March 22 (Egypt, Iraq, Jordan, Lebanon, Saudi Arabia, Syria and Yemen)',
  'countries': ['YE'],
  'sentiment': '#2F9599 '
},{
  'year': 2120,
  'description': '1945: Fifty states sign the Charter of the United Nations on June 26',
  'countries': [],
  'sentiment': None
}, {
  'year': 2120,
  'description': '1945–1950: Chinese Civil War between the nationalist Kuomintang and the Communist Party led by Mao Zedong',
  'countries': ['CN'],
  'sentiment': '#EC2049'
}, {
  'year': 1960,
  'description': '1946–1954: First Indochina War',
  'countries': ['VN'],
  'sentiment': '#EC2049'
}, {
  'year': 1800,
  'description': '1947: Official start of the Cold War (see Cold War (1947-1953) and Cold War (1953-1962))',
  'countries': ['RU'],
  'sentiment': '#F26B38'
}, {
  'year': 1800,
  'description': '1947: Independence of India and of Pakistan (Pakistan came into being on August 14, and India on August 15)[6]',
  'countries': ['IN'],
  'sentiment': '#2F9599 '
},  {
  'year': 1800,
  'description': '1947: Independence of India and of Pakistan (Pakistan came into being on August 14, and India on August 15)[6]',
  'countries': ['PK'],
  'sentiment': '#2F9599 '
},{
  'year': 1800,
  'description': '1947: UN Resolution 181 on the partition of Palestine in favor of a Two-state solution.',
  'countries': ['PS'],
  'sentiment': '#F26B38'
}, {
  'year': 1800,
  'description': '1947: French repression of the Malagasy uprising. 90 to 100 000 killed.',
  'countries': ['MG'],
  'sentiment': '#EC2049'
}, {
  'year': 1640,
  'description': '1948: Declaration of the establishment of the State of Israel on May 14 and first Arab-Israeli War',
  'countries': ['IL'],
  'sentiment': '#F26B38'
}, {
  'year': 1640,
  'description': '1948: Colonial exhibition in Belgium',
  'countries': ['BE'],
  'sentiment': '#2F9599 '
}, {
  'year': 1480,
  'description': "1949: Proclamation of the People's Republic of China by Mao Zedong",
  'countries': ['CN'],
  'sentiment': '#2F9599 '
}, {
  'year': 1160,
  'description': "1951: Publication of Hannah Arendt's The Origins of Totalitarianism (second section dedicated to imperialism)",
  'countries': [],
  'sentiment': None
}, {
  'year': 1000,
  'description': '1952: Alf#EC2049 Sauvy coins the term "Third World"',
  'countries': [],
  'sentiment': None
}, {
  'year': 680,
  'description': '1954: French establishments in India cease to exist after de facto transfer to the Indian Union (de jure union accomplished in 1962)',
  'countries': ['IN'],
  'sentiment': '#2F9599 '
}, {
  'year': 680,
  'description': '1954: Battle of Dien Bien Phu & 1954 Geneva Accords marks the end of French Indochina',
  'countries': ['VN'],
  'sentiment': '#2F9599 '
}, {
  'year': 520,
  'description': '1955: Bandung Conference',
  'countries': ['ID'],
  'sentiment': '#2F9599 '
}, {
  'year': 360,
  'description': "1956: Suez Crisis between Israel, the UK and France against Egypt, after Nasser's nationalisation of the Suez Canal Company",
  'countries': ['EG'],
  'sentiment': '#F26B38'
}, {
  'year': 200,
  'description': "1957: Algerian independence militant Larbi Ben M'Hidi murde#EC2049 in prison, early March",
  'countries': ['DZ'],
  'sentiment': '#F26B38'
}, {
  'year': 200,
  'description': '1957: First country sub-Saharan Africa (Ghana) regains independence.',
  'countries': ['GH'],
  'sentiment': '#2F9599 '
}, {
  'year': 40,
  'description': '1958: Foundation of the United Arab Republic as a first step toward a Pan-Arab nation; it is formed by Egypt and Syria (until 1961). Creation also of the short-term Arab Federation of Iraq and Jordan.',
  'countries': ['SY'],
  'sentiment': '#2F9599 '
}, {
  'year': 120,
  'description': '1959: Independence of Morocco and Tunisia',
  'countries': ['MA'],
  'sentiment': '#2F9599 '
}, {
  'year': 120,
  'description': '1959: Independence of Morocco and Tunisia',
  'countries': ['TN'],
  'sentiment': '#2F9599 '
}, {
  'year': 280,
  'description': '1960: Independence of French colonies in Africa; the UN reach 99 members states',
  'countries': [],
  'sentiment': None
}, {
  'year': 440,
  'description': '1961: Assassination of Patrice Lumumba, first prime minister of the Democratic Republic of the Congo, on January 17',
  'countries': ['CG'],
  'sentiment': '#EC2049'
}, {
  'year': 440,
  'description': '1961: Formation of the Conferência das Organizações Nacionalistas das Colónias Portuguesas on April 18 in Casablanca, Morocco (PAIGC, MPLA, FRELIMO and MLSTP)',
  'countries': ['MA'],
  'sentiment': '#2F9599 '
}, {
  'year': 440,
  'description': '1961: Creation of the Non-Aligned Movement',
  'countries': ['RU'],
  'sentiment': '#2F9599 '
}, {
  'year': 440,
  'description': '1961: Soviet premier Khrushchev declares that the Soviet Union would support all "national liberation movements"',
  'countries': ['RU'],
  'sentiment': None
}, {
  'year': 440,
  'description': "1961: Publication of Frantz Fanon' The Wretched of the Earth",
  'countries': [],
  'sentiment': -0.643158
}, {
  'year': 440,
  'description': '1961: October 17 Paris massacre',
  'countries': ['FR'],
  'sentiment': None
}, {
  'year': 440,
  'description': '1961: Indian annexation of Goa ends Portuguese India (Goa, Dadra, Nagar Haveli, Daman and Diu).',
  'countries': ['IN'],
  'sentiment': '#2F9599 '
}, {
  'year': 440,
  'description': '1961–1974: Portuguese Colonial War; See also Angolan War of Independence (1961-1989)',
  'countries': ['AO'],
  'sentiment': '#2F9599 '
}, {
  'year': 600,
  'description': '1962: Évian Accords halts the Algerian War and puts end to French rule in North-Africa',
  'countries': ['DZ'],
  'sentiment': '#2F9599 '
}, {
  'year': 760,
  'description': '1963: Assassination of Sylvanus Olympio on January 13, first president of Togo; he is replaced by Gnassingbé Eyadéma, who ruled over Togo until his death in 2005',
  'countries': ['TG'],
  'sentiment': '#F26B38'
}, {
  'year': 1080,
  'description': '1965–1975: Vietnam War',
  'countries': ['VN'],
  'sentiment': '#EC2049'
}, {
  'year': 1080,
  'description': '1965: Assassination of Mehdi Ben Barka, leader of the UNPF and of the Tricontinental Conference',
  'countries': ['MA'],
  'sentiment': '#F26B38'
}, {
  'year': 1080,
  'description': '1965: Joseph Mobutu becomes the dictator of the Democratic Republic of Congo until his overthrow in 1997 by Laurent-Désiré Kabila',
  'countries': ['CG'],
  'sentiment': '#F26B38'
}, {
  'year': 1400,
  'description': '1967: Assassination of Che Guevara in Bolivia.',
  'countries': ['BO'],
  'sentiment': '#F26B38'
}, {
  'year': 1720,
  'description': '1969: Assassination of Eduardo Mondlane, leader of the FRELIMO',
  'countries': [],
  'sentiment': None
}, {
  'year': 1880,
  'description': '1970s: Independence of the former Portuguese colonies, following the April 25, 1974 Carnation Revolution and the Portuguese Colonial War',
  'countries': ['PT'],
  'sentiment': '#2F9599 '
}, {
  'year': 2040,
  'description': '1971: Independence of Bangladesh following the war with Pakistan',
  'countries': ['BD'],
  'sentiment': '#2F9599 '
}, {
  'year': 2040,
  'description': "1971: Publication of Eduardo Galeano's Open Veins of Latin America[7]",
  'countries': [],
  'sentiment': None
}, {
  'year': 2040,
  'description': "1971: Publication of Gustavo Gutiérrez's A Theology of Liberation: History, Politics, Salvation[8]",
  'countries': [],
  'sentiment': None
}, {
  'year': 2360,
  'description': '1973: Assassination of Amilcar Cabral, leader of the African Party for the Independence of Guinea and Cape Verde (PAIGC) on January 20',
  'countries': ['CV'],
  'sentiment': '#EC2049'
}, {
  'year': 2360,
  'description': '1973: The PAIGC proclaims the independence of Guinea-Bissau on September 24',
  'countries': ['GW'],
  'sentiment': '#2F9599 '
}, {
  'year': 2680,
  'description': "1975: Portugal recognizes Mozambique's independence on June 25 and Angola on November 11",
  'countries': ['MZ'],
  'sentiment': '#2F9599 '
}, {
  'year': 2680,
  'description': "1975: Portugal recognizes Mozambique's independence on June 25 and Angola on November 11",
  'countries': ['AO'],
  'sentiment': '#2F9599 '
}, {
  'year': 2648,
  'description': '1979: Soviet invasion of Afghanistan and start of the "Second Cold War"',
  'countries': ['AF'],
  'sentiment': '#EC2049'
}, {
  'year': 2488,
  'description': '1980: The UN reaches 154 member states',
  'countries': [],
  'sentiment': None
}, {
  'year': 2488,
  'description': '1980: Assassination of Óscar Romero, prelate archbishop of San Salvador and proponent of the Liberation theology, on March 24',
  'countries': ['SV'],
  'sentiment': '#F26B38'
}, {
  'year': 2168,
  'description': '1982: Latin American debt crisis (in particular in Mexico, Brazil and Argentina)',
  'countries': ['MX'],
  'sentiment': '#F26B38'
},  {
  'year': 2168,
  'description': '1982: Latin American debt crisis (in particular in Mexico, Brazil and Argentina)',
  'countries': ['BR'],
  'sentiment': '#F26B38'
},  {
  'year': 2168,
  'description': '1982: Latin American debt crisis (in particular in Mexico, Brazil and Argentina)',
  'countries': ['AR'],
  'sentiment': '#F26B38'
},  {
  'year': 1208,
  'description': '1988: Assassination of Dulcie September, member of the African National Congress',
  'countries': [],
  'sentiment': None
}, {
  'year': 1048,
  'description': '1989: Operation Just Cause against Manuel Noriega',
  'countries': [],
  'sentiment': -0.293424
}, {
  'year': 888,
  'description': '1990: Independence of Namibia, the UN reaches 159 states.',
  'countries': ['NA'],
  'sentiment': '#2F9599 '
}, {
  'year': 248,
  'description': "1994: Nelson Mandela becomes president of South Africa in the nation's first all race election",
  'countries': ['ZA'],
  'sentiment': '#2F9599 '
}, {
  'year': 872,
  'description': '2001: French law recognizing slavery and the Atlantic slave trade as crimes against humanity (Taubira Law)',
  'countries': ['FR'],
  'sentiment': '#2F9599 '
}, {
  'year': 1512,
  'description': '2005: February 23 French law on the "positive aspects" of "French presence abroad, in particular in North Africa"',
  'countries': ['FR'],
  'sentiment': '#2F9599 '
}, {
  'year': 1672,
  'description': '2006: Repeal of the February 23, 2005 French law, following criticisms of historical revisionism',
  'countries': [],
  'sentiment': None
}, {
  'year': 2312,
  'description': '2010: Dissolution of the Netherlands Antilles',
  'countries': ['NL'],
  'sentiment': '#2F9599 '
}]

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
	"GL": "#2F9599 land",
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

sim_dataset = run_model()[-20:]

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    cnmap = [tuple(reversed(x)) for x in country_map.items()]
    #dataset = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19 , 20, 21, 22]
    form = InputForm()
    if form.validate_on_submit():
        flash('Requested for handles {} {}'.format(
            form.fst_handle.data, form.snd_handle.data))
        return #EC2049irect(url_for('index'))
    return render_template('index.html', title='Home', sim_dataset = sim_dataset, cnmap = cnmap, dataset=dataset,form=form)
