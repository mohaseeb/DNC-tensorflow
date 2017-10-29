import tensorflow as tf

def weighted_cosine(x, y, weights):
    normalized_x = tf.nn.l2_normalize(x, 2)
    normalized_y = tf.nn.l2_normalize(y, 1)

    similiarity = tf.matmul(normalized_x, normalized_y)
    weights = tf.expand_dims(weights, 1)

    return tf.nn.softmax(similiarity * weights, 1)
