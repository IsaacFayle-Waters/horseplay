# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#Items relevent to results page crawl, and subsequent model. 
class ResultItem(scrapy.Item):
    h_name = scrapy.Field()
    h_uid = scrapy.Field()
    wgt = scrapy.Field()
    co_code = scrapy.Field()#horse country code
    
    finish = scrapy.Field()
    draw = scrapy.Field()
    age  = scrapy.Field()
    OR = scrapy.Field()
    rpr = scrapy.Field()
    ts = scrapy.Field()
    sp = scrapy.Field()
    length =scrapy.Field()#lengths behind winner. Poss define default?

    trainer_uid = scrapy.Field()
    trainer_url = scrapy.Field()
        
    jockey_uid = scrapy.Field()
    jockey_wgt_al = scrapy.Field()
    jockey_url = scrapy.Field()

    sire_uid = scrapy.Field()
    dam_uid = scrapy.Field()
    damSire_uid = scrapy.Field()

    course_n = scrapy.Field()
    race_id = scrapy.Field()
    race_type = scrapy.Field()
    going = scrapy.Field()
    distance = scrapy.Field()
    round_distance = scrapy.Field()
    class_r = scrapy.Field()

    race_time = scrapy.Field()
    race_date = scrapy.Field()

    test = scrapy.Field() 

#More for initial test, and use specifically with racecards, as opposed to results.
class HoresplayoneItem(scrapy.Item):
    
    #Runner details
    h_name = scrapy.Field()
    h_uid = scrapy.Field()
    draw = scrapy.Field()
    finish = scrapy.Field()
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

#For use with posible pedegree features, eventually.  
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

