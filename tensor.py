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
    #y_data = data[-1].astype(np.float32)  # 1행 6열
    x_data = preprocessing.normalize(x_data[1:], norm='l2')
    #x_data = np.insert(x_data, 0, basis, 0)
    for i in range(0, len(x_data)):
        for j in range(0, len(x_data)):
            if (i >= j):
                pass
            else:
                Var.append(basis)
                Var.append(x_data[i])
                Var.append(x_data[j])
                #Var.append(y_data)
                FinalData.append((Var))
                Var = []
    return FinalData




df = pd.read_excel('BankruptcyStock.xls')
xy = df.as_matrix().transpose()

# print(xy[0], xy[-1])        # [ 1.  1.  1.  1.  1.  1.] [ 0.  0.  0.  1.  1.  1.]



#x_data = xy[3:-1].astype(np.float32)            # 3행 6열
y_data = xy[-1].astype(np.float32)             # 1행 6열
#basis = x_data[0]
#x_data = preprocessing.normalize(x_data[5:], norm='l2')
#x_data = np.insert(x_data, 0, basis, 0)

x_data = MakeVar(xy)

for i in range(0,len(x_data)):
    X = tf.placeholder(tf.float32)
    Y = tf.placeholder(tf.float32)

    W = tf.Variable(tf.random_uniform([1, len(x_data[0])], -1.0, 1.0))

    h = tf.matmul(W, X)
    hypothesis = tf.div(1., 1. + tf.exp(-h))    # exp(-h) = e ** -h. e는 자연상수

    cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))

    rate = tf.Variable(0.2)
    optimizer = tf.train.GradientDescentOptimizer(rate)
    train = optimizer.minimize(cost)

    init = tf.global_variables_initializer()

    sess = tf.Session()
    sess.run(init)

    for step in range(2001):
        sess.run(train, feed_dict={X: x_data[i], Y: y_data})
        if step % 20 == 0:
            sess.run(cost, feed_dict={X: x_data[i], Y: y_data}), sess.run(W)
            #print(step, sess.run(cost, feed_dict={X: x_data[i], Y: y_data}), sess.run(W))

    print('-----------------------------------------')

    # 결과가 0 또는 1로 계산되는 것이 아니라 0과 1 사이의 값으로 나오기 때문에 True/False는 직접 판단

    df = pd.read_excel('BankruptcyStock(test).xls')
    xy = df.as_matrix().transpose()



    x_data = MakeVar(xy)
    y_data = xy[-1].astype(np.float32)             # 1행 6열

    score = 0
    for j in range(0,len(x_data[0][0])):


        #print('[', x_data[i][0][j], x_data[i][1][j], x_data[i][2][j], y_data[j],']: ',sess.run(hypothesis, feed_dict={X: [[x_data[i][0][j]], [x_data[i][1][j]], [x_data[i][2][j]] ]}) > 0.7)
        if((sess.run(hypothesis, feed_dict={X: [[x_data[i][0][j]], [x_data[i][1][j]], [x_data[i][2][j]] ]}) > 0.5)[0][0] == y_data[j]):
            score = score + 1

    print(len(x_data[0][0]), '중', score,'점')


    sess.close()

