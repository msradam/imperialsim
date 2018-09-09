# ImperialSim

## Background
Imperialism and Colonialism are viewed as relics of days-gone-by, but numerous modern institutional problems - ranging from racism to economic inequality and global warming- stem as a result of these phenomena
    
There is also a lack of understanding in colonialism's global impact, with many localizing its influence and thus underestimating the extent to which Western influence - and malevolence - have spread throughout the world.

This website offers a compact look at imperialism's spread since Columbus sailed the ocean blue, through a chronological survey at how different nations and reaches of the world have been affected by policies at home and across the pond. 

# How We Build It

We used BeautifulSoup4 and a [Wikipedia Python library](https://pypi.org/project/wikipedia/) to scrape [Wikipedia timelines of Western colonialism](https://en.wikipedia.org/wiki/Chronology_of_Western_colonialism), then implemented high-efficiency functional programming to map large datasets to get the information we needed. Using that data, we manipulated SVG components to effectively show where colonialism has had its impact. We also enabled an option in a backend to use agent-based simulation data based off of the historical data we collected. The web app was created using Python Flask and deployed it using Google Cloud's App Engine

# Simulation

![Alt Text](https://media.giphy.com/media/u0kMhFnHnp7buekvkF/giphy.gif)

RED countries - or landmasses that were formerly not of any nation - have been either negatively impacted by imperialism or have had their influence severely diminished, either way, resulting in loss of life or structural violence. 

ORANGE countries are undergoing conflict or dispute - perhaps an assassination has occured, or there is a controversial conference - and GREEN countries are freer of imperial grasp, either having gained their independence or forming Empires of their own.
