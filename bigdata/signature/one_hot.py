import csv
import tensorflow as tf

filename = '/mnt/f/coding/bigdata/signature/train.csv'

tr_lab_indices = []
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
						tr_lab_indices.append(int(item))
					else:
						pic.append(int(item))
					c += 1
				train_data.append(pic)
			r += 1
			c = 0
except csv.Error as e:
	print("Eorror reading csv file at line %s:%s" % (reader.line_num,e))
	sys.exit(-1)
	
#creat tensor
indices = tf.constant(tr_lab_indices, tf.int64)

train_label = tf.one_hot(indices, 10, 1, 0, -1)
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
#sess.run(train_label)

#print(train_label)
with tf.Session():
	print(train_label.eval())


	