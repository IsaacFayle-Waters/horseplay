import scrapy


class RacecardSpider(scrapy.Spider):
    name = 'raceCard'
    allowed_domains = ['www.racingpost.com']
    start_urls = ['https://www.racingpost.com/racecards/13/chester/2023-05-10/838120/']

    def parse(self, response):
          cardHead = response.css('.RC-courseHeader')
          card = response.css('.RC-runnerCardWrapper')

          yield{
          		'course' : cardHead.css('.RC-courseHeader__name::text').get(default='').strip(),
          		'time'	 : cardHead.css('.RC-courseHeader__time::text').get(default='').strip(),
          		'date'	 : cardHead.css('.RC-courseHeader__date::text').get(default='').strip(),
          		'distance' : cardHead.css('span[data-test-selector="RC-header__raceDistance"]::text').get(default='').replace('(','').replace(')','').strip(),
          		'title'	 : cardHead.css('span[data-test-selector="RC-header__raceInstanceTitle"]::text').get(default='').strip(),
          		} 
          for horse in card:
          	yield{
          		'name': horse.css('.RC-runnerName::text').get(default='').strip(),
          		'draw': horse.css('.RC-runnerNumber__draw::text').get(default='').strip(' \n()'),
          		'age' : horse.css('.RC-runnerAge::text').get(default='').strip(),
          		'OR'  : horse.css('.RC-runnerOr::text').get(default='').strip(),
          		'Rpr' : horse.css('.RC-runnerRpr::text').get(default='').strip(),
          		'Ts'  : horse.css('.RC-runnerTs::text').get(default='').strip(),
          		'Tr'  : horse.css('.js-RC-runnerInfo_rtf::text').get(default='').strip(),
          		'form': horse.css('.RC-runnerInfo__form').get(default='')
          		.replace('<span class="RC-runnerInfo__form" data-test-selector="RC-cardPage-runnerForm">\n','')
          		.replace('</span>','').replace('<b>','').replace('</b>','').strip(), 
          	}
