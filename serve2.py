import tensorflow as tf

# 모델 불러오기
sess = tf.Session()
saver = tf.train.import_meta_graph('model2.meta')
saver.restore(sess, tf.train.latest_checkpoint('./'))

graph = tf.get_default_graph()

X = tf.placeholder(tf.float32, shape=[None, 7])
keep_prob = tf.placeholder(tf.float32)

W1 = graph.get_tensor_by_name("W1:0")
B1 = graph.get_tensor_by_name("B1:0")
L1 = tf.nn.relu(tf.matmul(X, W1) + B1)
L1 = tf.nn.dropout(L1, keep_prob=keep_prob)

W2 = graph.get_tensor_by_name("W2:0")
B2 = graph.get_tensor_by_name("B2:0")
L2 = tf.nn.relu(tf.matmul(L1, W2) + B2)
L2 = tf.nn.dropout(L2, keep_prob=keep_prob)

W3 = graph.get_tensor_by_name("W3:0")
B3 = graph.get_tensor_by_name("B3:0")
L3 = tf.nn.relu(tf.matmul(L2, W3) + B3)
L3 = tf.nn.dropout(L3, keep_prob=keep_prob)

W4 = graph.get_tensor_by_name("W4:0")
B4 = graph.get_tensor_by_name("B4:0")
L4 = tf.nn.relu(tf.matmul(L3, W4) + B4)
L4 = tf.nn.dropout(L4, keep_prob=keep_prob)

W5 = graph.get_tensor_by_name("W5:0")
B5 = graph.get_tensor_by_name("B5:0")
hypothesis = tf.matmul(L4, W5) + B5


def betting(card1, card2, my_chip, com_chip, my_bet, com_bet, bet_count):
    return sess.run(hypothesis, feed_dict={X: [[card1, card2, my_chip, com_chip, my_bet, com_bet, bet_count]], keep_prob: 1})[0][0]
