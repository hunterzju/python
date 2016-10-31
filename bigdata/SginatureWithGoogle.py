#!/usr/bin python3
#!coding UTF-8

import csv
import tensorflow as tf

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
	
# print(train_label)
# for datarow in train_data:
	# print(datarow)

#train use TensorFlow

#compute model
x = tf.placeholder(tf.float32,[None,784])

W = tf.Variable(tf.zeros[784,10])
b = tf.Variable(tf.zeros[10])

y = tf.nn.softmax(tf.matmul(x,W) + b)

#cross entrop to train
y_ = tf.placeholder(tf.float32,[None,10])
cross_entrop = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entrop)

#start session
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(200):
	xs = []
	ys = []
	for m in range(100):
		xs.append(train_data[i*100+m])
		ys.append(train_label[i*100+m])
	sess.run(train_step,feed_dict{x:xs,y :ys})




	
