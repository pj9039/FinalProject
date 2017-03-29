import tensorflow as tf
import numpy as np


import pandas as pd

import numpy as np
from sklearn import preprocessing

df = pd.read_excel('BankruptcyStock.xls')
xy = df.as_matrix().transpose()

# print(xy[0], xy[-1])        # [ 1.  1.  1.  1.  1.  1.] [ 0.  0.  0.  1.  1.  1.]

x_data = xy[3:-1].astype(np.float32)            # 3행 6열
y_data = xy[-1].astype(np.float32)             # 1행 6열
x_data = preprocessing.normalize(x_data, norm='l2')

print(x_data[0][0])
print(x_data[1][0])
print(x_data[2][0])
print(x_data[3][0])
print(x_data[4][0])
