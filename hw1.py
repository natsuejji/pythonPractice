import csv 
import numpy as np
import random
import math
import sys
import os

data = []
# 每一個維度儲存一種污染物的資訊
for i in range(18):
	data.append([])

n_row = 0
# load data
with open('data/train.csv', 'r', encoding='big5') as t:
	row = csv.reader(t , delimiter=",")
	for r in row:
		if n_row != 0:
			for i in range(3,27):
				if r[i] !="NR":
					data[(n_row-1)%18].append(float(r[i]))
				else:
					data[(n_row-1)%18].append(float(0))
		n_row += 1

x = []
y = []
# parse data
for i in range(12):
	# 一個月取連續10小時的data可以有471筆
    for j in range(471):
        x.append([])
		#18種汙染
        for t in range(18):
            # 連續9小時
            for s in range(9):
                x[471*i+j].append(data[t][480*i+j+s] )
        y.append(data[9][480*i+j+9])
x = np.array(x)
y = np.array(y)

# add square term
# x = np.concatenate((x,x**2), axis=1)

# add bias
x = np.concatenate((np.ones((x.shape[0],1)),x), axis=1)

# init weight and  l_Rate
w = np.zeros(len(x[0]))
l_rate = 10
repeat = 10000
hypo = np.zeros(len(x[0]))

# gradient descent: adagrad	
x_t = x.transpose()
s_gra = np.zeros(len(x[0]))
for i in range(repeat):
	hypo = np.dot(x,w) # y_predict = dot (x, weight)
	loss = hypo - y # LOSS = Y^ - Y 所以這裡的LOSS是負的
	cost = np.sum(loss**2) / len(x) #LOSS FUNCIOTN == 平方差  (除以len(x) => normalization)
	cost_a  = math.sqrt(cost) #C(x) = summation over all (y_train-y_predict)**2
	gra = 2*np.dot(x_t, loss) # partial c(theta^t) / partial w^t = 
	s_gra += gra**2			  #summation over all 2 * (y_train - y_predict) * - w^t
	ada = np.sqrt(s_gra)
	w = w - l_rate * gra/ada
	print ('iteration: %d | Cost: %f  ' % ( i, cost_a))

#SAVE WEIGTH
# save model
np.save('model.npy', w)
# read model
w = np.load('model.npy')

# read test file

test_x = []
n_row = 0
text = open('data/test.csv' ,"r")
row = csv.reader(text , delimiter= ",")

for r in row:
    if n_row %18 == 0:
        test_x.append([])
        for i in range(2,11):
            test_x[n_row//18].append(float(r[i]) )
    else :
        for i in range(2,11):
            if r[i] !="NR":
                test_x[n_row//18].append(float(r[i]))
            else:
                test_x[n_row//18].append(0)
    n_row = n_row+1
text.close()
test_x = np.array(test_x)

# add square term
# test_x = np.concatenate((test_x,test_x**2), axis=1)

# add bias
test_x = np.concatenate((np.ones((test_x.shape[0],1)),test_x), axis=1)

# get ans.csv

ans = []
for i in range(len(test_x)):
    ans.append(["id_"+str(i)])
    a = np.dot(w,test_x[i])
    ans[i].append(a)

filename = "predict.csv"

with open(filename, "w+") as text:
	s = csv.writer(text,delimiter=',',lineterminator='\n')
	s.writerow(["id","value"])
	for i in range(len(ans)):
	    s.writerow(ans[i])