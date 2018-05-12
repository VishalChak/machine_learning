import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

result  = x1*x2
#result = tf.mul(x1,x2) IN python 3 tensorflow does not have mul fuction
print(result)

with tf.Session() as sess:
    output = sess.run(result)
    print(output)
print(output)


