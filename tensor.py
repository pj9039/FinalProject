import tensorflow as tf
import numpy as np

# 04train.txt
# #x0 x1 x2 y
# 1   2   1   0
# 1   3   2   0
# 1   3   5   0
# 1   5   5   1
# 1   7   5   1
# 1   2   5   1
import pandas as pd

import numpy as np
from sklearn import preprocessing

def MakeVar(data):
    Var = []
    FinalData = []
    x_data = data[3:-1].astype(np.float32)  # 3행 6열
    basis = x_data[0]
    x_data = preprocessing.normalize(x_data[1:], norm='l2')
    for i in range(0, len(x_data)):
        for j in range(0, len(x_data)):
            if (i >= j):
                pass
            else:
                Var.append(basis)
                Var.append(x_data[i])
                Var.append(x_data[j])
                Var.append(i)
                Var.append(j)
                FinalData.append((Var))
                Var = []
    return FinalData

def MakeVar1(data):
    Var = []
    FinalData = []
    x_data = data[3:-1].astype(np.float32)  # 3행 6열
    basis = x_data[0]
    x_data = preprocessing.normalize(x_data[1:], norm='l2')
    for i in range(0, len(x_data)):
        for j in range(0, len(x_data)):
            if (i >= j):
                pass

            for k in range(0,len(x_data)):
                if (i >= j):
                    pass
                if (j>=k):
                    pass
                if (i >= k):
                    pass
                else:
                    Var.append(basis)
                    Var.append(x_data[i])
                    Var.append(x_data[j])
                    Var.append(x_data[k])
                    Var.append(i)
                    Var.append(j)
                    Var.append(k)
                    FinalData.append((Var))
                    Var = []
    return FinalData


df = pd.read_excel('BankruptcyStock.xls')
df1 = pd.read_excel('BankruptcyStock.xls', header=None)
xy = df.as_matrix().transpose()
xy1 = df1.as_matrix().transpose()
x_data1 = xy1[1:][3:-1] # 3행 6열
#x_data = xy[3:-1].astype(np.float32)            # 3행 6열
y_data = xy[-1].astype(np.float32)             # 1행 6열
x_data = MakeVar(xy)
x_data2 = MakeVar1(xy)
print(x_data2)
x_dataTitle = []
for i in range(0,len(x_data1)):
    x_dataTitle.append(x_data1[i][:1])
'''
for i in range(0,len(x_data)):
    X = tf.placeholder(tf.float32)
    Y = tf.placeholder(tf.float32)

    W = tf.Variable(tf.random_uniform([1, len(x_data[0][:-2])], -1.0, 1.0))
    h = tf.matmul(W, X)
    hypothesis = tf.div(1., 1. + tf.exp(-h))    # exp(-h) = e ** -h. e는 자연상수
    cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
    rate = tf.Variable(0.2)
    optimizer = tf.train.GradientDescentOptimizer(rate)
    train = optimizer.minimize(cost)
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    for step in range(3001):
        sess.run(train, feed_dict={X: x_data[i][:-2], Y: y_data})
        if step % 20 == 0:
            sess.run(cost, feed_dict={X: x_data[i][:-2], Y: y_data}), sess.run(W)
            #print(step, sess.run(cost, feed_dict={X: x_data[i][:-2], Y: y_data}), sess.run(W))
    print('-----------------------------------------')
    # 결과가 0 또는 1로 계산되는 것이 아니라 0과 1 사이의 값으로 나오기 때문에 True/False는 직접 판단
    df = pd.read_excel('BankruptcyStock(test).xls')
    xy = df.as_matrix().transpose()
    x_dataTest = MakeVar(xy)
    y_dataTest = xy[-1].astype(np.float32)             # 1행 6열
    score = 0
    for j in range(0,len(x_dataTest[0][0])):
        #print('[', x_dataTest[i][0][j], x_dataTest[i][1][j], x_dataTest[i][2][j], y_dataTest[j],']: ',sess.run(hypothesis, feed_dict={X: [[x_dataTest[i][0][j]], [x_dataTest[i][1][j]], [x_dataTest[i][2][j]] ]}) > 0.7)
        if((sess.run(hypothesis, feed_dict={X: [[x_dataTest[i][0][j]], [x_dataTest[i][1][j]], [x_dataTest[i][2][j]] ]}) > 0.6)[0][0] == y_dataTest[j]):
            score = score + 1
    print('변수1: ',x_dataTitle[x_data[i][-2]],'변수2: ',x_dataTitle[x_data[i][-1]], '적중률: ', round((score/len(x_dataTest[0][0]))*100,2),'%')
    sess.close()
'''
for i in range(0,len(x_data2)):
    X = tf.placeholder(tf.float32)
    Y = tf.placeholder(tf.float32)

    W = tf.Variable(tf.random_uniform([1, len(x_data2[0][:-3])], -1.0, 1.0))
    h = tf.matmul(W, X)
    hypothesis = tf.div(1., 1. + tf.exp(-h))    # exp(-h) = e ** -h. e는 자연상수
    cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
    rate = tf.Variable(0.2)
    optimizer = tf.train.GradientDescentOptimizer(rate)
    train = optimizer.minimize(cost)
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    for step in range(3001):
        sess.run(train, feed_dict={X: x_data2[i][:-3], Y: y_data})
        if step % 20 == 0:
            sess.run(cost, feed_dict={X: x_data2[i][:-3], Y: y_data}), sess.run(W)
            #print(step, sess.run(cost, feed_dict={X: x_data[i][:-2], Y: y_data}), sess.run(W))
    print('-----------------------------------------')
    # 결과가 0 또는 1로 계산되는 것이 아니라 0과 1 사이의 값으로 나오기 때문에 True/False는 직접 판단
    df = pd.read_excel('BankruptcyStock(test).xls')
    xy = df.as_matrix().transpose()
    x_dataTest = MakeVar1(xy)
    y_dataTest = xy[-1].astype(np.float32)             # 1행 6열
    score = 0
    for j in range(0,len(x_dataTest[0][0])):
        #print('[', x_dataTest[i][0][j], x_dataTest[i][1][j], x_dataTest[i][2][j], y_dataTest[j],']: ',sess.run(hypothesis, feed_dict={X: [[x_dataTest[i][0][j]], [x_dataTest[i][1][j]], [x_dataTest[i][2][j]] ]}) > 0.7)
        if((sess.run(hypothesis, feed_dict={X: [[x_dataTest[i][0][j]], [x_dataTest[i][1][j]], [x_dataTest[i][2][j]], [x_dataTest[i][3][j]] ]}) > 0.8)[0][0] == y_dataTest[j]):
            score = score + 1
    print('변수1: ',x_dataTitle[x_data2[i][-3]],'변수2: ',x_dataTitle[x_data2[i][-2]],'변수3: ',x_dataTitle[x_data2[i][-1]], '적중률: ', round((score/len(x_dataTest[0][0]))*100,2),'%')
    sess.close()