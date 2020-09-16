import tensorflow as tf
import numpy as np

# specify path to training data and testing data

train_x_location = "dataset_x_train.csv"
train_y_location = "dataset_y_train.csv"
test_x_location = "dataset_x_train.csv"
test_y_location = "dataset_y_train.csv"

print("Reading training data")
# each instance is stored as a row of m values
m = 2
# there are k classes
k = 2
x_train = np.loadtxt(train_x_location, dtype="uint8", delimiter=",")
y_train = np.loadtxt(train_y_location, dtype="uint8", delimiter=",")

# define the training model
model = tf.keras.models.Sequential([
    # input_shape should be specified in the first layer
    tf.keras.layers.Dense(1,
                          activation=tf.keras.activations.linear,
                          use_bias=False,
                          input_shape=(m,)),
    tf.keras.layers.Dense(2, activation=tf.nn.relu),
    tf.keras.layers.Dense(k, activation=tf.nn.softmax)
])

# options for optimizer: 'sgd' and 'adam'. sgd is stochastic gradient descent
# loss='mean_squared_error'
model.compile(optimizer='sgd',
              loss='mean_squared_error',
              metrics=['accuracy'])

print("train")
model.fit(x_train, y_train, epochs=10, batch_size=1)

print("Reading testing data")
x_test = np.loadtxt(test_x_location, dtype="uint8", delimiter=",")
y_test = np.loadtxt(test_y_location, dtype="uint8", delimiter=",")

print("evaluate")
model.evaluate(x_test, y_test, batch_size=1)