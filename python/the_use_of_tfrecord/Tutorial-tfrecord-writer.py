# -*- coding:utf-8 -*- 

import tensorflow as tf
import numpy as np
from tqdm import tqdm

'''tfrecord 写入数据.
将固定shape的矩阵写入 tfrecord 文件。
refer: http://blog.csdn.net/qq_16949707/article/details/53483493
'''

# **1.创建文件
writer1 = tf.python_io.TFRecordWriter('../data/test1.tfrecord')
writer2 = tf.python_io.TFRecordWriter('../data/test2.tfrecord')

X = np.arange(0, 100).reshape([50, -1]).astype(np.float32)  # 50个样本
y = np.arange(50)

for i in tqdm(xrange(len(X))):  # **2.对于每个样本
    if i > len(y) / 2:
        writer = writer1
    else:
        writer = writer2
    X_sample = X[i].tolist()
    y_sample = y[i]
    example = tf.train.Example(  # **3.定义数据类型，按照这里固定的形式写，有float_list(好像只有32位), int64_list, bytes_list.
        features=tf.train.Features(
            feature={'X': tf.train.Feature(float_list=tf.train.FloatList(value=X_sample)),
                     'y': tf.train.Feature(int64_list=tf.train.Int64List(value=[y_sample]))}))
    serialized = example.SerializeToString()
    writer.write(serialized)  # **4.写入文件中

print('Finished.')
writer1.close()
writer2.close()
