import tensorflow as tf
import numpy as np
from tensorflow import keras
'''
Sequential 序贯模型是多个网络层的线性堆叠
model.layers:组成模型图的各个层
model.inputs:模型的输入张量列表
model.outputs:模型的输出张量列表
'''

#units：大于0的整数,代表该层的输出维度
# 比如,一个一阶的张量[1,2,3]的shape是(3,);一个二阶的张量[[1,2,3],[4,5,6]]的shape是(2,3);
# 一个三阶的张量[[[1],[2],[3]],[[4],[5],[6]]]的shape是(2,3,1)。input_shape就是指输入张量的
#在keras中,数据是以张量的形式表示的,张量的形状称之为shape,表示从最外层向量逐步到达最底层向量的解包过程。
#activation=None：激活函数.但是默认 liner 

model = keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])

#函数编译模型以供训练,optimizer：优化器,为预定义优化器名或优化器对象, SGD:随机梯度下降法
#loss：目标函数,为预定义损失函数名或一个目标函数  mean_squared_error:计算预测值与真值的均方差
model.compile( optimizer='sgd',loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)


#训练模型 x：输入数据 y：标签  epochs：训练的轮数
model.fit(xs,ys, epochs=450)

#predict按batch获得输入数据对应的输出
print(model.predict([8.0]))

