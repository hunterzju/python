#!/usr/bin python3
#!coding UTF-8

import csv
import tensorflow as tf
import numpy as np

filename = '/mnt/f/coding/bigdata/signature/train.csv'
testfile = '/mnt/f/coding/bigdata/signature/test.csv'
csvfile = '/mnt/f/coding/bigdata/signature/result.csv'

tr_lab_indices = []
train_data = [[]]

#read train data
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
	
#read test data
test_data = []
try:
	with open(testfile) as ft:
		reader_t = csv.reader(ft)
		r = 0
		for row in reader_t:
			if r == 0:
				header_t = row
			else:
				pic = []
				for item in row:
					pic.append(int(item))
				test_data.append(pic)
			r += 1
except csv.Error as e:
	print("Eorror reading csv file at line %s:%s" % (reader.line_num,e))
	sys.exit(-1)

#convert label to one_hot
indices = tf.constant(tr_lab_indices, tf.int64)
train_label = tf.one_hot(indices, 10, 1, 0, -1)

#covert list to array
del train_data[0]
tr_data = np.array(train_data)
te_data = np.array(test_data,np.float32)

#train use TensorFlow

#compute model
x = tf.placeholder(tf.float32,[None,784])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W) + b)

#cross entrop to train
y_ = tf.placeholder(tf.float32,[None,10])
cross_entrop = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entrop)

#test data
t_x = tf.placeholder(tf.float32,[28000,784])
result = tf.nn.softmax(tf.matmul(t_x,W)+b)
result_tag = tf.argmax(result,1)

#start session
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

with tf.Session() as sess1:
	tr_label_list = train_label.eval().tolist()
	tr_label = np.array(tr_label_list)

sess.run(train_step,feed_dict={x:tr_data,y_:tr_label})

res_out = sess.run(result_tag,feed_dict={t_x:te_data})
	#res_out = result_tag.eval().tolist()
res_write = res_out.tolist()

#write_file = open(csvfile,'wb',newline="")
with open(csvfile,'w',newline='') as write_file:
	spamwriter = csv.writer(write_file,dialect='excel')
	for i in range(len(res_write)):
		spamwriter.writerow([int(res_write[i])])

write_file.close()	

#train 
#sess.run(train_step,feed_dict={x:tr_data,y_:tr_label})	

# #save the model
# saver = tf.train.Saver()
# with tf.Session() as sess1:
# 	saver.restore(sess1,"/mnt/f/coding/bigdata/signature/model.ckpt")
# 	print("save model success!")
	
# #test
#print(sess.run(result_tag,feed_dict={t_x:te_data}))



# for i in range(280):
# 	test_batch = []
# 	for j in range(100):
# 		test_batch.append(test_data[i*100+j])
# 	te_batch = np.array(test_batch,float32)
# 	sess.run(result,feed_dict={t_x:te_batch})

#print(result_tag)


	
