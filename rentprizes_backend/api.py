# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask_cors import CORS
import json
import os
import json

# flask server for scraper data delivering.

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
working_directory = os.getcwd()

scraping_date = '01_23'


# req: http://127.0.0.1:5000/getScrapingDates
# response: scraping dates in analitycs folder f.e ['01_23', '12_22']
@app.route('/getScrapingDates')
def getScrapingDates():
    return [ f.name for f in os.scandir(f'{working_directory}\\analitycs') if f.is_dir() ]

# req: http://127.0.0.1:5000/getDataByDistrict?city=krakow&date=01_23
# res: average prizes by room ([1 room average, 2 room average, 3 room average, 4+ rooms average]) and  district f.e [{"district_name": "Kraków, Krowodrza", "district_prizes": [2072, 2906, 3487, 3259]}, {"district_name": "Kraków, Prądnik Biały", "district_prizes": [2036, 2625, 3037, 5090]}, {"district_name": "Kraków, Bieżanów-Prokocim", "district_prizes": [1818, 2344, 2898, 3718]}, {"district_name": "Kraków", "district_prizes": [2444, 2940, 3025, 4717]}, {"district_name": "Kraków, Podgórze Duchackie", "district_prizes": [1952, 2448, 3052, 0]}, {"district_name": "Kraków, Grzegórzki", "district_prizes": [2143, 3069, 4285, 5594]}, {"district_name": "Kraków, Podgórze", "district_prizes": [2162, 2914, 3909, 5952]}, {"district_name": "Kraków, Prądnik Czerwony", "district_prizes": [2123, 2572, 3145, 3127]}, {"district_name": "Kraków, Dębniki", "district_prizes": [2044, 2618, 3819, 4670]}, {"district_name": "Kraków, Stare Miasto", "district_prizes": [2399, 3139, 4993, 5174]}, {"district_name": "Kraków, Nowa Huta", "district_prizes": [1889, 2411, 2888, 0]}, {"district_name": "Kraków, Łagiewniki-Borek Fałęcki", "district_prizes": [2030, 2640, 3365, 3206]}, {"district_name": "Kraków, Zwierzyniec", "district_prizes": [1803, 3311, 4090, 7000]}, {"district_name": "Kraków, Bieńczyce", "district_prizes": [1704, 2331, 2834, 3170]}, {"district_name": "Kraków, Bronowice", "district_prizes": [1952, 2822, 3077, 5300]}, {"district_name": "Kraków, Czyżyny", "district_prizes": [2014, 2726, 3571, 0]}, {"district_name": "Kraków, Swoszowice", "district_prizes": [1700, 2691, 3509, 0]}, {"district_name": "Kraków, Wzgórza Krzesławickie", "district_prizes": [1740, 2297, 2609, 0]}, {"district_name": "Kraków, Mistrzejowice", "district_prizes": [1671, 2559, 2688, 3258]}]
@app.route('/getDataByDistrict')
def getDataByDistrict():
    city = request.args.get('city')
    date = request.args.get('date')
    data = None
    with open(f'{working_directory}\\analitycs\\{date}\\{city}-analitycs.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data

# req: http://127.0.0.1:5000/getAveragePrizes?city=krakow&date=01_23
# res: averages of prizes only by room in specific city f.e [1984.0,2703.32,3383.21,4516.79]
@app.route('/getAveragePrizes')
def getAveragePrizes(incity=None, indate=None):
    city = request.args.get('city') if request.args.get('city') else incity
    date = request.args.get('date') if request.args.get('date') else indate

    data = None
    averages = [[], [], [], []]
    with open(f'{working_directory}\\analitycs\\{date}\\{city}-analitycs.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
    
    for district in data:
        for i in range(4):
            averages[i].append(district['district_prizes'][i]) if district['district_prizes'][i] != 0 else None

    averages = list(map(lambda x: round(sum(x) / len(x) if len(x) > 0 else 0, 2), averages))

    return averages

# req: http://127.0.0.1:5000/getPrizesHistory?city=krakow
# res: history of prizes by scraping dates f.e [{"date":"12_22","values":[2004.89,2712.79,3586.33,5157.5]},{"date":"01_23","values":[1984.0,2703.32,3383.21,4516.79]}]
@app.route('/getPrizesHistory')
def getPrizesHistory():
    city = request.args.get('city')
    dates = getScrapingDates()
    dates.sort(key = lambda x: x.split('_')[1])
    data = []
    for date in dates:
        data.append({
            "date": date,
            "values": getAveragePrizes(city, date)
        })
    return data

if __name__ == "__main__":
    app.run()