import csv
from datetime import datetime

class Temperature:
	name = ""
	date = ""
	avg = ""
	max = ""
	min = ""

	def __init__(self, name, date, avg, max, min):
		self.name = name
		self.date = datetime.strptime(date, '%Y-%m-%d')
		#print(avg)
		self.avg = float(avg)
		self.max = max
		self.min = min
	
	def __repr__(self):
		return '{'+self.name+', '+str(self.date)+', '+str(self.avg)+', '+str(self.max)+', '+str(self.min)+'}'

def get_date(temperature):
    return temperature.get('date')

def GetData():
	result = []

	with open('weather-data/2755795.csv', 'r') as f:
		rowNumber = 0
		reader = csv.reader(f)
		for row in reader:
			if rowNumber > 0 and len(row[3]) > 0:
				item = Temperature(row[1], row[2], row[3], row[4], row[5])
				result.append(item)
			rowNumber += 1
	return result

def main():
	print("main")
	data = GetData()

	for x in range(1943, 2021):
	
		year = x

		data.sort(key=lambda x: x.date)
		find_elements = [p for p in data if
			#p.name == "RIGA, LG" and
			p.date >= datetime(year, 1, 1) and p.date < datetime(year + 1, 1, 1)
		]
		elements_count = len(find_elements)		
		temp_sum = sum(el.avg for el in find_elements)
		if elements_count > 0:
			average_year = round(temp_sum / elements_count, 2)
		else:
			average_year = 0
		#print("Count: " + str(elements_count))
		#print("Sum: " + str(temp_sum))
		print(str(year) + ": " + str(average_year))

if __name__ == "__main__":
	print("start")
	main()
	print("stop")


