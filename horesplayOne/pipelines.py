# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
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
		
		if adapter.get('or_'):
			adapter['or_'] = int(adapter['or_'].replace('\u2013','0'))
		
		if adapter.get('rpr'):
			adapter['rpr'] = int(adapter['rpr'].replace('\u2013','0'))

		if adapter.get('ts'):
			adapter['ts'] = int(adapter['ts'].replace('\u2013','0'))
			
		return item

class SetDefaultPipeline:
	def process_item(self,item,spider):
		for field in item.fields:
			item.setdefault(field, 'NULL')

		return item


class DatabasePipeline:
	def __init__(self):
		self.con = sqlite3.connect('testScrape.db')
		self.cur = self.con.cursor()
		self.create_table()

	def create_table(self):
		self.cur.execute("""CREATE TABLE IF NOT EXISTS horses(h_name TEXT,
															  h_uid INTEGER,
															  wgt INTEGER,
															   co_code TEXT,
															   finish TEXT,
															   draw INTEGER,
															   age INTEGER,
															   or_ INTEGER,
															   rpr INTEGER,
															   ts INTEGER,
															   sp REAL,
															   length REAL,
															   trainer_uid INTEGER,
															   trainer_url TEXT,
															   jockey_uid INTEGER,
															   jockey_wgt_al INTEGER,
															   jockey_url TEXT,
															   sire_uid INTEGER,
															   dam_uid INTEGER,
															   damSire_uid INTEGER,
															   course_n TEXT,
															   race_id INTEGER,
															   race_type TEXT,
															   going TEXT,
															   distance REAL,
															   class_r INTEGER,
															   race_time TEXT,
															   race_date TEXT)""")


	def process_item(self,item,spider):
		self.cur.execute("""INSERT INTO horses VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
							(item['h_name'], item['h_uid'], item['wgt'],item['co_code'],
								item['finish'], item['draw'], item['age'], item['or_'], item['rpr'], item['ts'],
								 item['sp'], item['length'], item['trainer_uid'], item['trainer_url'], item['jockey_uid'],
								  item['jockey_wgt_al'], item['jockey_url'], item['sire_uid'], item['dam_uid'], item['damSire_uid'],
								   item['course_n'], item['race_id'], item['race_type'], item['going'], item['distance'],
								    item['class_r'], item['race_time'], item['race_date']))
		self.con.commit()

		return item