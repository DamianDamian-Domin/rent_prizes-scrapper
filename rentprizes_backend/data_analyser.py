import json
import os
from functions import Analyzer

# script that removes duplicate bids from scraper and creates basic analytics data needed for server flask


working_directory = os.getcwd()

scraping_date = '02_23'

# get newest data from scraper
cities = ['krakow', 'warszawa', 'wroclaw', 'poznan', 'lodz']
for city in cities:

    file_data = None

    # open file, remove duplicates, save modified file
    with open(f'{working_directory}\\..\\rentprizes_scraper\\rentprizes_scraper\\results\\{scraping_date}\\{city}.json', 'r', encoding="utf-8") as file:
        file_data = json.load(file)
        file_data = [dict(t) for t in {tuple(d.items()) for d in file_data}]

    with open(f'{working_directory}\\..\\rentprizes_scraper\\rentprizes_scraper\\results\\{scraping_date}\\{city}.json', 'w', encoding="utf-8") as file:
        json.dump(file_data, file, ensure_ascii=False, indent=4)

    # create analitycs files for cities
    analyzer = Analyzer(file_data)
    with open(f'{working_directory}\\analitycs\\{scraping_date}\\{city}-analitycs.json', 'w', encoding="utf-8") as outfile:
        json.dump(analyzer.getDataCombo(), outfile, ensure_ascii=False)