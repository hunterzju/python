#!/usr/bin python3
#!coding UTF-8

import csv
import tensorflow as tf

filename = '/home/coding/python/bigdata/signature/train.csv'

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
						tr_lab_indices.append(item)
					else:
						pic.append(int(item))
					c += 1
				train_data.append(pic)
			r += 1
			c = 0
except csv.Error as e:
	print("Eorror reading csv file at line %s:%s" % (reader.line_num,e))
	sys.exit(-1)
	
#convert label to one_hot
indices = tf.constant(tr_lab_indices, tf.int64)
train_label = tf.one_hot(indices, 10, 1, 0, -1)

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
with tf.Session():
	tr_label = train_label.eval()

for i in range(200):
	xs = []
	ys = []
	for m in range(100):
		xs.append(train_data[i*100+m])
		ys.append(tr_label[i*100+m])
	sess.run(train_step,feed_dict={x:xs,y_:ys})

with tf.Session():
	print(W.eval())
	print("==========================")
	print(b.eval())


	
