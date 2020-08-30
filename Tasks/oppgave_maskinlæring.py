import tensorflow as tf 
from tensorflow import keras

import matplotlib as plt
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)

model = tf.keras.models.Sequential()

# sørger for å flatne netverket slik at det får en trekantform mot slutten
model.add(tf.keras.layers.Flatten())

# 'model' bør ha dybde eller bredde (lennyface) for nøyaktige resultater
model.add(tf.keras.layers.Dense(200, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(80, activation = tf.nn.relu))
# 'softmax' viktig for nøyaktige resultater
# antallet 'nodes' må også tilsvare mulige svaralternativer, under 10 funker ikke
model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(x_train, y_train, epochs = 3)

val_loss, val_accuracy = model.evaluate(x_test, y_test)
print(val_loss, val_accuracy)
# legge til tredje 'vet ikke' klasse?
class_labels = ['Cat', 'Dog']



#print(tf.__version__)
#print(x_train[0])