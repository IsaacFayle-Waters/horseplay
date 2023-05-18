import scrapy
import json
from horesplayOne.items import HorseProfileItem

class HorseprofileSpider(scrapy.Spider):
    name = 'horseProfile'
    allowed_domains = ['www.racingpost.com']
    start_urls = ['http://www.racingpost.com/profile/horse/3056464/lakota-warrior/form']

    def parse(self, response):
    	#string of javascript with horse info in json format
        js: str = response.css('body script::text')[0].get()
        #find start and end points of json section
        start = js.find('=')
        end = js.find('}};')        
        js_str = js[start+2:end+2]
        hdjson = json.loads(js_str)
        

        horse = HorseProfileItem()
        profile = hdjson["profile"]
        trainer14 = profile["trainerLast14Days"]
        medical = profile["medical"][0]

        horse["h_name"] = profile["horseName"]
        horse["h_uid"] = profile["horseUid"]
        horse["c_origin"] = profile["horseCountryOriginCode"]
        horse["h_sex"] = profile["horseSexCode"]

        horse["sire_c_origin"] = profile["sireCountryOriginCode"]
        horse["sire_avg_flat"] =profile["sireAvgFlatWinDist"]
        horse["sire_avg_dist"] =profile["sireAvgWinDistance"]
        
        horse["dam_c_origin"] = profile["damCountryOriginCode"]
        
        horse["damSire_c_origin"] = profile["damSireCountryOriginCode"]
        horse["damSire_avg_flat"] = profile["damSireAvgFlatWinDist"]
        horse["damSire_avg_dist"] = profile["damSireAvgWinDistance"]
        
        horse["trainer_name"] = profile["trainerName"]
        horse["trainer_uid"] =profile["trainerUid"]
        horse["trainer_14_perc"] = trainer14["percent"]
        horse["trainer_14_runs"] = trainer14["runs"]
        horse["trainer_14_wins"] = trainer14["wins"]

        horse["medical"] = medical["medicalType"]


        yield horse





