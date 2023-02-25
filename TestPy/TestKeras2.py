import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# ini a Matrix 1000 * 1000 row 1000, col 1000, random number
data = np.random.random((1000,100))

#print(data)

# ini a arrar 1000 * 1, value 0 or 1   random number
labels = np.random.randint(2, size=(1000,1))

#print(labels)

model = Sequential()

# 32 network laier   aloth relu
model.add(Dense(32,
                activation='relu',
                input_dim=100))

model.add(Dense(1,
                activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(data, labels, epochs=10, batch_size=32)
predictions = model.predict(data)

