
class Analyzer():

    def __init__(self, file_data):
        self.districts = []
        self.file_data = file_data


    def stripNumber(self, number):
        return float(number.replace('zł', '').replace(' ', '').replace(',', '.')) 

    def arrayAverage(self, lst):
        arr = list(filter(lambda a: a != 0, lst))
        if len(arr) == 0:
            return 0
        return sum(arr) / len(arr)

    def getAllDistricts(self):
        for offer in self.file_data:
            self.districts.append(offer['location']) if offer['location'] not in self.districts else None

    def filterByDistrict(self, district):
        return list(filter(lambda x: x['location'] == district, self.file_data))

    def getAveragePrizes(self, data):
        data_by_rooms = [[] for _ in range(4)]
        for x in data:
            data_by_rooms[x['rooms']-1].append(self.stripNumber(x['price']))
        for i in range(len(data_by_rooms)):
            data_by_rooms[i] = list(filter(lambda value: value < 15000, data_by_rooms[i]))
            if len(data_by_rooms[i]) > 4: 
                data_by_rooms[i] = round(self.arrayAverage(data_by_rooms[i]))
            else:
                data_by_rooms[i] = 0
        return data_by_rooms

    def getDataCombo(self):
        self.getAllDistricts()
        data_combo = []
        for district in self.districts:
            data_combo.append({
                "district_name": district,
                "district_prizes": self.getAveragePrizes((self.filterByDistrict(district)))
            })
        return data_combo