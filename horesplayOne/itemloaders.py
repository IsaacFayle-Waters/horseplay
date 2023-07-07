from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader

class ResultLoader(ItemLoader):
	default_output_processor = TakeFirst()
	h_name_in = MapCompose(lambda x : x.strip())
	h_uid_in = MapCompose(lambda x : x.split('/')[-2])
	#wgt_in = MapCompose(lambda x : x.strip()) 
	#wgt_out = Join('-')
	finish_in = MapCompose(lambda x : x.split())
	draw_in =  MapCompose(lambda x : x.strip().replace('(','').replace(')',''))
	age_in = MapCompose(lambda x : x.strip())
	or__in = MapCompose(lambda x : x.strip())
	rpr_in = MapCompose(lambda x : x.strip())
	ts_in  = MapCompose(lambda x : x.strip())
	sp_in = MapCompose(lambda x : x.strip())
	co_code_in = MapCompose(lambda x : x.strip().replace('(','').replace(')',''))
	
	jockey_uid_in = MapCompose(lambda x :x.split('/')[-2])
	trainer_uid_in = MapCompose(lambda x :x.split('/')[-2]) 
	sire_uid_in = MapCompose(lambda x :x.split('/')[-2])
	dam_uid_in = MapCompose(lambda x :x.split('/')[-2])
	damSire_uid_in = MapCompose(lambda x :x.split('/')[-2])
		
	course_n_in = MapCompose(lambda x : x.strip())
	class_r_in = MapCompose(lambda x : x.strip().replace('(Class ','').replace(')',''))
	distance_in = MapCompose(lambda x : x.strip())
	going_in  = MapCompose(lambda x : x.strip())
	race_date_in = MapCompose(lambda x : x.strip())
	race_time_in = MapCompose(lambda x : x.strip())

	test_in = MapCompose(lambda x : x.strip())

class RaceCardLoader(ResultLoader):
	race_id_in = MapCompose(lambda x :x.split('/')[-1])
	jockey_wgt_al_in = MapCompose(lambda x : x.strip())