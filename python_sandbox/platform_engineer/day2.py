import datetime

def population():
	swaziland_pop = 42000
	swazilant_growth_rate = 1.03
	djibouti_pop = 54000
	djibouti_growth_rate = 1.02

	years = 0
	while True:
		if swaziland_pop > djibouti_pop:
			break
		else:
			swaziland_pop *= swazilant_growth_rate
			djibouti_pop *= djibouti_growth_rate
			years += 1
	print years

def three_second_hello_world():
	stop_time = datetime.datetime.now() + datetime.timedelta(seconds=3)
	while datetime.datetime.now() < stop_time:
		print "Hello World! " + str(datetime.datetime.now())

dict1 = {'id': "first_thing", 'name': 'ball', 'category': 'sports'}
dict2 = {'id': "second_thing", 'name': 'shoe', 'category': 'footware'}
dict3 = {'id': "third_thing", 'name': 'juice', 'category': 'drink'}
dict_list = [dict1, dict2, dict3]

def sequence_of_dictionaries(dicts):
	dict_comp = {map_obj['id']:map_obj for map_obj in dicts}
	print dict_comp

def time_strategy(time_amount_int, time_measurement_str):
	def seconds(seconds_int):
		return datetime.timedelta(seconds=seconds_int)
	def minutes(minutes_int):
		return datetime.timedelta(minutes=minutes_int)
	def hours(hours_int):
		return datetime.timedelta(hours=hours_int)
	strategy = {'seconds': seconds,
				'minutes': minutes,
				'hours': hours}
	print strategy[time_measurement_str](time_amount_int)



if __name__ == '__main__':
	population()
	three_second_hello_world()
	sequence_of_dictionaries(dict_list)
	time_strategy(32, 'hours')