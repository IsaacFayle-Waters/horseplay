import scrapy


class ResultsSpider(scrapy.Spider):
    name = 'results'
    allowed_domains = ['www.racingpost.com']
    
    #START FROM DATE PROVIDED ON CRAWL (i.e. scrapy crawl results -a date = 2022-05-17 )
    def start_requests(self):
    	date = self.date
    	url = 'http://racingpost.com/results/' + date + '/time-order'
    	yield scrapy.Request(url, callback = self.getUrls)
    #GET URLS OF ALL RACES ON THAT DAY
    async def getUrls(self, response):
        linkTable = response.css('a[data-test-selector="link-listCourseNameLink"]::attr(href)')

        for slug in linkTable:
        	url = 'http://www.racingpost.com'
        	yield scrapy.Request(url + slug.get(), callback=self.parse)
    #DO STUFF    	
    async def parse(self, response):


    	for url in response.css('a[data-test-selector="link-horseName"]::text'):
    		yield{'url':url.get().strip()}
