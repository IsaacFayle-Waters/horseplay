import scrapy
from horesplayOne.items import HoresplayoneItem

class RacecardtwoSpider(scrapy.Spider):
    name = 'raceCardTwo'
    allowed_domains = ['racingpost.com']
    start_urls = ['http://racingpost.com/racecards/time-order']

    #retreive urls from list of day's races
    def parse(self, response):
  
    	urls = response.css('.RC-meetingItem__link::attr(href)')
    	pri = len(urls)
    	for url in urls:
    		pri = pri - 1
    		yield scrapy.Request('http://racingpost.com' + url.get(), callback = self.parse2, priority=pri)

    #scrape horse and race details from each of the day's races. Race details added to each horse.
    def parse2(self, response):
    	card = response.css('.RC-runnerCardWrapper , .RC-courseHeader, .RC-headerBox')
    	#course
    	course = card.css('.RC-courseHeader__name::text').get(default='').strip()
    	#race details
    	win_money = card.css('div[data-test-selector="RC-headerBox__winner"] div::text')[1].get()
    	num_runners = card.css('div[data-test-selector="RC-headerBox__runners"] div::text')[1].get().strip()
    	going = card.css('div[data-test-selector="RC-headerBox__going"] div::text')[1].get()
    	distance = card.css('span[data-test-selector="RC-header__raceDistance"]::text').get(default='').replace('(','').replace(')','').strip()
    	round_distance = card.css('strong[data-test-selector="RC-header__raceDistanceRound"]::text').get().strip()
    	class_r = card.css('span[data-test-selector="RC-header__raceClass"]::text').get(default='').replace('(','').replace(')','').strip()
    	#temporal concerns
    	time = card.css('.RC-courseHeader__time::text').get(default='').strip()
    	date = card.css('.RC-courseHeader__date::text').get(default='').strip()
    	 
    	#loop over each horse, extract details. 
    	h_item = HoresplayoneItem()
    	for horse in card:
    		h_item['h_name'] = horse.css('.RC-runnerName::text').get(default='').strip()
    		h_item['draw'] = horse.css('.RC-runnerNumber__draw::text').get(default='').strip(' \n()')
    		h_item['age'] = horse.css('.RC-runnerAge::text').get(default='').strip()
    		h_item['OR'] = horse.css('.RC-runnerOr::text').get(default='').strip()
    		h_item['rpr'] = horse.css('.RC-runnerRpr::text').get(default='').strip()
    		h_item['ts'] = horse.css('.RC-runnerTs::text').get(default='').strip()
    		h_item['tr'] = horse.css('.js-RC-runnerInfo_rtf::text').get(default='').strip()
    		h_item['form'] = horse.css('.RC-runnerInfo__form').get(default='').replace('<span class="RC-runnerInfo__form" data-test-selector="RC-cardPage-runnerForm">\n','').replace('</span>','').replace('<b>','').replace('</b>','').strip()

    		h_item['course'] = course
    		h_item['going'] = going
    		h_item['no_runner'] = num_runners
    		h_item['class_r'] = class_r
    		h_item['race_time'] = time
    		h_item['race_date'] = date
    		
    		h_item['distance'] = distance
    		h_item['round_distance'] = round_distance
    		    		   		
    		h_item['win_money']	= win_money
    		yield h_item   	