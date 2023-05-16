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
