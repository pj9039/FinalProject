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

df = pd.read_excel('BankruptcyStock.xls')
xy = df.as_matrix().transpose()

# print(xy[0], xy[-1])        # [ 1.  1.  1.  1.  1.  1.] [ 0.  0.  0.  1.  1.  1.]

x_data = xy[3:-1].astype(np.float32)            # 3행 6열
y_data = xy[-1].astype(np.float32)             # 1행 6열
basis = x_data[0]
x_data = preprocessing.normalize(x_data[5:], norm='l2')
x_data = np.insert(x_data, 0, basis, 0)
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
print(x_data)

# feature별 가중치를 난수로 초기화. feature는 bias 포함해서 3개. 1행 3열.
W = tf.Variable(tf.random_uniform([1, len(x_data)], -1.0, 1.0))

# 행렬 곱셈. (1x3) * (3x6)
h = tf.matmul(W, X)
hypothesis = tf.div(1., 1. + tf.exp(-h))    # exp(-h) = e ** -h. e는 자연상수

# exp()에는 실수만 전달
# print(tf.exp([1., 2., 3.]).eval())      # [2.71828175 7.38905621 20.08553696]
# print(tf.exp([-1., -2., -3.]).eval())   # [0.36787945 0.13533528 0.04978707]

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))

rate = tf.Variable(0.2)
optimizer = tf.train.GradientDescentOptimizer(rate)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(2001):
    sess.run(train, feed_dict={X: x_data, Y: y_data})
    if step % 20 == 0:
        print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))

print('-----------------------------------------')

# 결과가 0 또는 1로 계산되는 것이 아니라 0과 1 사이의 값으로 나오기 때문에 True/False는 직접 판단

df = pd.read_excel('BankruptcyStock(test).xls')
xy = df.as_matrix().transpose()

# print(xy[0], xy[-1])        # [ 1.  1.  1.  1.  1.  1.] [ 0.  0.  0.  1.  1.  1.]

x_data = xy[3:-1].astype(np.float32)            # 3행 6열
basis = x_data[0]
x_data = preprocessing.normalize(x_data[5:], norm='l2')
x_data = np.insert(x_data, 0, basis, 0)

y_data = xy[-1].astype(np.float32)             # 1행 6열

for i in range(0, len(x_data[0])):
    #y_pred = sess.run(hypothesis , feed_dict={X: x_data})
    #correct_prediction = tf.equal(tf.cast(tf.argmax(hypothesis,1), tf.float32), Y)
    #accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    #print ("Accuracy: ",(sess.run(accuracy, feed_dict={X: x_data, Y: y_data})))
    print('[', x_data[0][i], x_data[1][i], x_data[2][i], x_data[3][i], y_data[i],']: ',sess.run(hypothesis, feed_dict={X: [[x_data[0][i]], [x_data[1][i]], [x_data[2][i]], [x_data[3][i]] ]}) > 0.8)
    #print('[', x_data[0][i], x_data[1][i], x_data[2][i], y_data[i],']: ',sess.run(hypothesis, feed_dict={X: [[x_data[0][i]], [x_data[1][i]], [x_data[2][i]] ]}) > 0.8 )


sess.close()

