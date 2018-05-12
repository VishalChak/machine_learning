import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

class deepnet:
    def deep_net(self):
        mnist  = input_data.read_data_sets("/temp/data/",one_hot=True)



if __name__ == "__main__":
    obj = deepnet()
    obj.deep_net()




