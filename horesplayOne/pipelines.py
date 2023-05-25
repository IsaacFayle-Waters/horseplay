# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HoresplayonePipeline:
    def process_item(self, item, spider):
        return item


class DistancePipeline:
	def process_item(self,item,spider):
		adapter = ItemAdapter(item)
		#REMOVE LETTERS AND UNICODE
		#CONVERT TO TOTAL FURLONGS RETURN FLOAT 
		if adapter.get('distance'):
			distance = adapter['distance'].replace('\u00bd','.5')
			distance = distance.replace("f","")
			distance = distance.split('m')
			if len(distance) == 1:
				distance = float(distance[0])
			else:
				distance[0].replace('m','')
				distance[0] = float(distance[0]) * 8
				if distance[1] == '':
					distance = float(distance[0])
				else:
					distance = distance[0] + float(distance[1])
				
			adapter['distance'] = distance
			return item


class SpPipeline:
	def process_item(self,item,spider):
		adapter = ItemAdapter(item)

		if adapter.get('sp'):
			adapter['sp'] = adapter['sp'].replace('F','').replace('J','').replace('Evens','1/1')
			num,den = adapter['sp'].split('/')
			num,den = int(num),int(den)
			odds = (den / (num + den))
			adapter['sp'] = odds
			return item


class DatatypePipeline:
	def process_item(self,item,spider):
		adapter = ItemAdapter(item)

		if adapter.get('draw'):
			adapter['draw'] = int(adapter['draw'])
		
		if adapter.get('age'):
			adapter['age'] = int(adapter['age'])
		
		if adapter.get('OR'):
			adapter['OR'] = int(adapter['OR'].replace('\u2013','0'))
		
		if adapter.get('rpr'):
			adapter['rpr'] = int(adapter['rpr'].replace('\u2013','0'))

		if adapter.get('ts'):
			adapter['ts'] = int(adapter['ts'].replace('\u2013','0'))
			
		return item