#Reconviened to scrape odds from sites other than Racingpost
from horesplayOne.scrapeToolsNonRP import getBookieString
from horesplayOne.items import HoresplayoneItem
import scrapy

#def getBookieString(h_name,bookie):
#  return '[data-runner="' + str(h_name) + '"]'+ ' [data-bookmaker="'+ bookie +'"] div::text'

class RacecardSpider(scrapy.Spider):
    name = 'raceCard'
    start_urls =['https://www.horseracing.net/racecards']
    
    def parse(self,response):
        urls = response.css('.result-box a::attr(href)')
        #pri = len(urls)
        for url in urls:
          if url.get().split('/')[1] != 'results':
         #pri = pri - 1
            yield scrapy.Request('https://www.horseracing.net' + url.get(), callback = self.parse2)#, priority=pri )
    
    def parse2(self, response):
          resRow = response.css('.results-row')
          course,date,time = response.url.split('/')[3:]
          h_item =  HoresplayoneItem()
          for horse in resRow:
            name = horse.css('.person-name::text').get(default='').strip()
            if name != 'Each Way Terms':
              h_item['h_name'] = horse.css('.person-name::text').get(default='').strip()
              h_item['course_n'] = course
              h_item['race_date'] = date
              h_item['race_time'] = time 

              bookie = getBookieString(name,'betfair')
              h_item['odds_betfair'] = horse.css(bookie).get()
              bookie = getBookieString(name,'boylesports')
              h_item['odds_boylesports'] = horse.css(bookie).get()
              bookie = getBookieString(name,'paddypower')
              h_item['odds_paddypower'] = horse.css(bookie).get()
              bookie = getBookieString(name,'bet365')
              h_item['odds_bet365'] = horse.css(bookie).get()
              bookie = getBookieString(name,'williamhill')
              h_item['odds_williamhill'] = horse.css(bookie).get()
              bookie = getBookieString(name,'betvictor')
              h_item['odds_betvictor'] = horse.css(bookie).get()
              bookie = getBookieString(name,'betfred')
              h_item['odds_betfred'] = horse.css(bookie).get()
              bookie = getBookieString(name,'sbk')
              h_item['odds_sbk'] = horse.css(bookie).get()
              yield h_item
