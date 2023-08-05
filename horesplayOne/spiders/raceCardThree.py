import scrapy
#from scrapy_selenium import SeleniumRequest
from horesplayOne.items import ResultItem,RaceCardItem
from horesplayOne.itemloaders import RaceCardLoader
from horesplayOne.scrapeTools import wgtStripper, raceTypeGet


class RacecardthreeSpider(scrapy.Spider):
    name = 'raceCardThree'
    custom_settings = {
        'ITEM_PIPELINES': {
        'horesplayOne.pipelines.SetDefaultPipeline': 200,
        'horesplayOne.pipelines.SpPipeline': 300,
        'horesplayOne.pipelines.DistancePipeline': 400,
        'horesplayOne.pipelines.DatatypePipeline': 500,
        'horesplayOne.pipelines.DatabasePipeline': 600,
    }
    }
    allowed_domains = ['racingpost.com']
    start_urls = ['https://www.racingpost.com/racecards/time-order']

    def parse(self, response):
    	urls = response.css('.RC-meetingItem__link::attr(href)')
    	pri = len(urls)
    	for url in urls:
    		pri = pri - 1
    		yield scrapy.Request('http://racingpost.com' + url.get(), callback = self.parse2, priority=pri)

    async def parse2(self, response):
    	race_info = response.css('.RC-courseHeader, .RC-headerBox')
    	horses = response.css('.RC-runnerRow')
    	#per race details, for classification
    	course_n = response.css('.RC-courseTime__link::text').get().strip().replace('                             ','').replace('  ',' ')
    	race_time = race_info.css('.RC-courseHeader__time::text').get()
    	race_date = race_info.css('.RC-courseHeader__date::text').get()
    	going = race_info.css('div[data-test-selector="RC-headerBox__going"] div::text')[1].get()
    	distance = race_info.css('strong[data-test-selector="RC-header__raceDistanceRound"]::text').get() 
    	class_r = race_info.css('span[data-test-selector="RC-header__raceClass"]::text').get()
    	race_id = response.url

    	title = response.css('[data-test-selector="RC-header__raceInstanceTitle"]::text').get().strip()
    	race_type = raceTypeGet(title,course_n) 

    	#per horse details
    	for horse in horses:
    		result = RaceCardLoader(item=RaceCardItem(), selector = horse)
    		result.add_css('h_name', '.RC-runnerName::text')
    		result.add_css('h_uid', '.RC-runnerName::attr(href)')
    		wgt =  wgtStripper(horses.css('[data-order-wgt]').get())
    		result.add_value('wgt', wgt)
    		
    		result.add_css('draw', '.RC-runnerNumber__draw::text')
    		result.add_css('age', '.RC-runnerAge::text')
    		result.add_css('or_', '.RC-runnerOr::text')
    		result.add_css('rpr', '.RC-runnerRpr::text')
    		result.add_css('ts', '.RC-runnerTs::text')
    		#result.add_css('sp', '')
    		#result.add_css('co_code', '')
    		
    		result.add_css('jockey_uid', '.RC-runnerInfo_jockey a::attr(href)')
    		
    		result.add_css('jockey_wgt_al','[data-test-selector="RC-cardPage-runnerJockey-allowance"]::text')
    		result.add_css('trainer_uid','.RC-runnerInfo_trainer a::attr(href)')
    		result.add_css('sire_uid', '[data-test-selector="RC-pedigree__sire"]::attr(href)')
    		result.add_css('dam_uid', '[data-test-selector="RC-pedigree__dam"]::attr(href)')
    		result.add_css('damSire_uid','[data-test-selector="RC-pedigree__damsire"]::attr(href)')

    		result.add_value('course_n',course_n)
    		result.add_value('race_type',race_type)
    		result.add_value('going', going)
    		result.add_value('distance', distance)
    		result.add_value('class_r', class_r)
    		result.add_value('race_time',race_time)
    		result.add_value('race_date',race_date)
    		result.add_value('race_id',race_id)

    		yield result.load_item()