"""
Pre-defined network models.
"""

import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPool2D, BatchNormalization, Flatten, Dense, Activation, \
                                    GlobalAveragePooling2D


def make_omniglot_cnn_model(num_output_classes):
    model = tf.keras.models.Sequential()
    for i in range(4):
        if i == 0:
            model.add(Conv2D(filters=64, kernel_size=3, strides=1, padding="same", activation=None,
                             input_shape=[28, 28, 1]))

        else:
            model.add(Conv2D(filters=64, kernel_size=3, strides=1, padding="same", activation=None))

        model.add(BatchNormalization())
        model.add(MaxPool2D(pool_size=2, strides=2))
        model.add(Activation('relu'))

    model.add(Flatten())
    # model.add(GlobalAveragePooling2D())
    # model.add(Dense(256, activation=tf.nn.relu))
    model.add(Dense(num_output_classes, activation='softmax'))

    return model


def make_miniimagenet_cnn_model(num_output_classes, multi_headed=False, num_heads=-1):
    inputs = tf.keras.layers.Input(shape=(84, 84, 3), dtype=tf.float32)
    x = inputs
    for i in range(4):
        x = Conv2D(filters=32, kernel_size=3, strides=1, padding="same", activation=None)(x)
        x = BatchNormalization()(x)
        x = MaxPool2D(pool_size=2, strides=2, padding="same")(x)
        x = Activation('relu')(x)

    x = Flatten()(x)
    # model.add(GlobalAveragePooling2D())
    # model.add(Dense(256, activation=tf.nn.relu))

    if not multi_headed:
        x = Dense(num_output_classes, activation='softmax')(x)
    else:
        # Create 'num_heads' heads
        heads = []
        for i in range(num_heads):
            heads.append( Dense(num_output_classes, activation='softmax')(x) )
        x = tf.keras.layers.Concatenate(heads)

    model = tf.keras.models.Model(inputs=inputs, outputs=x) #[a, b])
    return model


def make_sinusoid_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation=tf.nn.relu, input_shape=[1]),
        tf.keras.layers.Dense(64, activation=tf.nn.relu),
        tf.keras.layers.Dense(1, activation='linear')
    ])
    return model
