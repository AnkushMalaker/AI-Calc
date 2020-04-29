
from tensorflow import keras
import tensorflow as tf
import numpy as np
import pandas as pd


df = pd.read_csv('dataset.csv')
x_train_first = keras.utils.to_categorical(df['number1'])
x_train_second = keras.utils.to_categorical(df['number2'])
y_train = keras.utils.to_categorical(df['result'])

dft = pd.read_csv('test.csv')
x_test_first = keras.utils.to_categorical(dft['number1'])
x_test_second = keras.utils.to_categorical(dft['number2'])
y_test = keras.utils.to_categorical(dft['result'])


print(x_train_first.shape)
print(x_train_second.shape)
print(y_train.shape)
print(x_test_first.shape)
print(x_test_second.shape)
print(y_test.shape)


a_input = keras.Input(shape=10)
b_input = keras.Input(shape=10)

concat1 = keras.layers.Concatenate()([a_input, b_input])
Dense1 = keras.layers.Dense(16)(concat1)
Dense2 = keras.layers.Dense(16)(Dense1)
output = keras.layers.Dense(19, activation='softmax')(Dense2)

model = keras.Model(inputs=[a_input, b_input], outputs=output)
model.summary()


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit([x_train_first,x_train_second], y_train, batch_size=1024, epochs=50, verbose=2, validation_split=0.01)


model.save("saved_model.md5")


def get_prediction(model, num1 ,num2):
    all = [0,1,2,3,4,5,6,7,8,9]
    all_coded = keras.utils.to_categorical(all)
    inp1 = all_coded[all.index(num1)]
    inp2 = all_coded[all.index(num2)]
    print(np.array([inp1, inp2]).shape)
    result = model([np.array([inp1]), np.array([inp2])])
    result_num = tf.argmax(result)
    if (np.sum(result_num)==0):
        return "...idk"
    else:
        return all[all_coded.index(result_num)]

print(get_prediction(model,3,4))


