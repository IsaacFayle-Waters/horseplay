import scrapy
from horesplayOne.scrapeTools import jsStripper

class QuickresultsSpider(scrapy.Spider):
    name = 'quickResults'
    allowed_domains = ['racingpost.com']
    
    #START FROM DATE PROVIDED ON CRAWL (i.e. scrapy crawl quickResults -a date = 2023-05-30 )
    def start_requests(self):
    	date = self.date
    	url = 'http://racingpost.com/results/' + date + '/time-order'
    	yield scrapy.Request(url, callback = self.getUrls)
    
    def getUrls(self, response):
    	raceitem = response.css('.rp-timeView__listItem')
    	url = 'http://www.racingpost.com'
    	for item in raceitem:
    		path = item.css('.rp-timeView__raceTitle a::attr(href)')
    		yield scrapy.Request(url + path.get(), callback=self.parse)

    def parse(self, response):
    	raceInfo = response.css('.rp-raceTimeCourseName')
    	tableSel = response.css('[data-test-selector="table-row"]')
    	
    	course_n = raceInfo.css('.rp-raceTimeCourseName__name::text').get().strip()
    	race_time = raceInfo.css('.rp-raceTimeCourseName__time::text').get()
    	race_date = raceInfo.css('.rp-raceTimeCourseName__date::text').get()

    	js = response.css('script')[12].get()
    	race_id = jsStripper(js,'raceId')
    	jScount = 0

    	for horse in tableSel:

    		yield{
    		"course_n": course_n,
    		"race_id" : race_id,
    		"h_uid"   : horse.css('a[data-test-selector="link-horseName"]::attr(href)').get().split('/')[-2],
    		"h_name" : horse.css('a[data-test-selector="link-horseName"]::text').get().strip(),
    		"finish" : horse.css('[data-test-selector="text-horsePosition"]::text').get().strip(),
    		"race_date" : race_date,
    		"race_time" : race_time,
    		}

