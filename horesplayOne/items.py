# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HoresplayoneItem(scrapy.Item):
    
    #Runner details
    h_name = scrapy.Field()
    draw = scrapy.Field()
    age  = scrapy.Field()
    OR = scrapy.Field()
    rpr = scrapy.Field()
    ts = scrapy.Field()
    tr = scrapy.Field()
    form = scrapy.Field()
    #race details
    course = scrapy.Field()
    win_money = scrapy.Field()
    no_runner = scrapy.Field()
    going = scrapy.Field()
    distance = scrapy.Field()
    round_distance = scrapy.Field()
    class_r = scrapy.Field()
    #time/date
    race_time = scrapy.Field()
    race_date = scrapy.Field()

class HorseProfileItem(scrapy.Item):
	h_name = scrapy.Field()
	h_uid =  scrapy.Field()
	h_sex = scrapy.Field()
	
	c_origin = scrapy.Field()
	sire_c_origin = scrapy.Field()
	sire_avg_flat = scrapy.Field()
	sire_avg_dist = scrapy.Field() 
	
	dam_c_origin = scrapy.Field()
	damSire_c_origin = scrapy.Field()
	damSire_avg_flat = scrapy.Field()
	damSire_avg_dist = scrapy.Field() 

	trainer_uid = scrapy.Field()
	trainer_name = scrapy.Field()
	trainer_14_perc = scrapy.Field()
	trainer_14_runs = scrapy.Field()
	trainer_14_wins = scrapy.Field()

	medical = scrapy.Field()

