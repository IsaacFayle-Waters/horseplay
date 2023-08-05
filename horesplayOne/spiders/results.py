import scrapy
import datetime
from horesplayOne.items import ResultItem
from horesplayOne.itemloaders import ResultLoader
from horesplayOne.scrapeTools import jsStripper

TESTING = False
TEST_INDEX = 0

class ResultsSpider(scrapy.Spider):
    name = 'results'
    custom_settings = {
    'ITEM_PIPELINES' : {
        'horesplayOne.pipelines.SetDefaultPipeline': 200,#not tested with results
        'horesplayOne.pipelines.SpPipeline': 300,
        'horesplayOne.pipelines.DistancePipeline': 400,
        'horesplayOne.pipelines.DatatypePipeline': 500,
        'horesplayOne.pipelines.DatabasePipeline': 600,
    }
    }
    allowed_domains = ['www.racingpost.com']
    
    #START FROM DATE PROVIDED ON CRAWL (i.e. scrapy crawl results -a date = 2023-05-30 )
    def start_requests(self):
    	date = self.date
    	url = 'http://racingpost.com/results/' + date + '/time-order'
    	yield scrapy.Request(url, callback = self.getUrls)
    
    #GET URLS OF ALL RACES ON THE DATE SUPPLIED ABOVE
    async def getUrls(self, response):
    	if TESTING == False:

    		#list of accepted countries (UK is automatically accepted)
    		accptList = ['(IRE)']
    		raceitem = response.css('.rp-timeView__listItem')
    		#if not UK race, and not Irish race, don't yield url
    		for item in raceitem:
    			#Don't record voided races 
    			if item.css('.rp-voidRace__description') or item.css('.rp-raceAbandoned'):
    				pass
    			else:
        			url = 'http://www.racingpost.com'
        			#If item has country code
        			if item.css('.rp-timeView__raceName__code::text').get():
        				cc = item.css('.rp-timeView__raceName__code::text').get().strip()
        				#If country code accepted, yield full url
        				if cc in accptList:
        					path = item.css('.rp-timeView__raceTitle a::attr(href)')
        					yield scrapy.Request(url + path.get(), callback=self.parse)
        			#If no code, it's a UK race, so yield
        			else:
        				path = item.css('.rp-timeView__raceTitle a::attr(href)')
        				try:
        					yield scrapy.Request(url + path.get(), callback=self.parse)
        				except TypeError:
        					pass   	
    	#TESTING ONLY
    	elif TESTING == True:
    		path = response.css('.rp-timeView__raceTitle a::attr(href)')[TEST_INDEX].get()
    		url = 'http://www.racingpost.com' + path
    		yield scrapy.Request(url, callback=self.parse)
    	
    	#Take the date added at start, advance date by one day, repeat until no more tomorrows.
    	y,m,d = self.date.split('-')
    	date = datetime.date(int(y),int(m),int(d))
    	delta = datetime.timedelta(days = 1)
    	date += delta
    	date = date.strftime("%Y-%m-%d")
    	self.date = date
    	next_page = 'https://www.racingpost.com/results/' + date + '/time-order'
    	
    	if next_page is not None:
    		yield response.follow(next_page,callback = self.getUrls)

    #PARSE INFORMATION PER HORSE PER RACE    	
    async def parse(self, response):
    	raceInfo = response.css('.rp-raceTimeCourseName')
    	tableSel = response.css('[data-test-selector="table-row"]')
    	#per race details, for classification
    	course_n = raceInfo.css('.rp-raceTimeCourseName__name::text').get()
    	race_time = raceInfo.css('.rp-raceTimeCourseName__time::text').get()
    	race_date = raceInfo.css('.rp-raceTimeCourseName__date::text').get()
    	going = raceInfo.css('.rp-raceTimeCourseName_condition::text').get()
    	distance = raceInfo.css('.rp-raceTimeCourseName_distance::text').get()
    	class_r = raceInfo.css('.rp-raceTimeCourseName_class::text').get()
    	#scraped from jsString
    	js = response.css('script')[12].get()
    	race_id = jsStripper(js,'raceId')
    	race_type = jsStripper(js,'raceTypeCode')
    	jScount = 0
    	
    	#per horse details
    	for horse in tableSel:
    		result = ResultLoader(item=ResultItem(), selector = horse)
    		result.add_css('h_name', 'a[data-test-selector="link-horseName"]::text')
    		result.add_css('h_uid', 'a[data-test-selector="link-horseName"]::attr(href)')
    		wgt = jsStripper(js,'wgtStNative','items',jScount)
    		result.add_value('wgt', wgt)
    		result.add_css('finish','[data-test-selector="text-horsePosition"]::text')
    		result.add_css('draw', '.rp-horseTable__pos__draw::text')
    		result.add_css('age', '[data-ending="yo"]::text')
    		result.add_css('or_','[data-ending="OR"]::text')
    		result.add_css('rpr','[data-ending="RPR"]::text')
    		result.add_css('ts','[data-ending="TS"]::text')
    		result.add_css('sp', '.rp-horseTable__horse__price::text')
    		length = jsStripper(js,'accumLengthNative','items',jScount)
    		result.add_value('length', length)
    		result.add_css('co_code', '.rp-horseTable__horse__country::text')
    		
    		result.add_css('jockey_uid', '[data-test-selector="link-jockeyName"]:not(.ui-link_marked)::attr(href)')
    		jockey_wgt_al = jsStripper(js,'wgtAllowance','items',jScount)
    		result.add_value('jockey_wgt_al',jockey_wgt_al)
    		result.add_css('trainer_uid','[data-test-selector="link-trainerName"]::attr(href)')
    		result.add_css('sire_uid', '[data-test-selector="table-row"] ~ [data-test-selector="block-pedigreeInfoFullResults"] td a:nth-child(1)::attr(href)')
    		result.add_css('dam_uid', '[data-test-selector="table-row"] ~ [data-test-selector="block-pedigreeInfoFullResults"] td a:nth-child(2)::attr(href)')
    		result.add_css('damSire_uid','[data-test-selector="table-row"] ~ [data-test-selector="block-pedigreeInfoFullResults"] td a:nth-child(3)::attr(href)')

    		result.add_value('course_n',course_n)
    		result.add_value('race_type',race_type)
    		result.add_value('going', going)
    		result.add_value('distance', distance)
    		result.add_value('class_r', class_r)
    		result.add_value('race_time',race_time)
    		result.add_value('race_date',race_date)
    		result.add_value('race_id',race_id)

    		result.add_css('jockey_url', '[data-test-selector="link-jockeyName"]:not(.ui-link_marked)::attr(href)')
    		result.add_css('trainer_url', '[data-test-selector="link-trainerName"]::attr(href)' )
    		
    		jScount = jScount + 1
    		yield result.load_item()