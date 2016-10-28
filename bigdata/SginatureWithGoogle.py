#!/usr/bin python3
#!coding UTF-8

import csv

filename = '/mnt/f/coding/bigdata/signature/train.csv'

train_label = []
train_data = [[]]

try:
	with open(filename) as f:
		reader = csv.reader(f)
		c = 0
		r = 0
		for row in reader:
			if r == 0:
				header = row
			else:
				pic = []
				for item in row:
					if c == 0:
						train_label.append(item)
					else:
						pic.append(int(item))
					c += 1
				train_data.append(pic)
			r += 1
			c = 0
except csv.Error as e:
	print("Eorror reading csv file at line %s:%s" % (reader.line_num,e))
	sys.exit(-1)
	
print(train_label)
for datarow in train_data:
	print(datarow)

	
