"""DNNClassifier for the Stack Overflow Developer Survey 2017 dataset."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf

import stack_data


parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,
                    help='number of training steps')

(train_x, train_y), (test_x, test_y) = None

def main(argv):
    args = parser.parse_args(argv[1:])

    # Fetch the stack_data
    (train_x, train_y), (test_x, test_y) = stack_data.get_test_train_data()
    print("Training Features Shape: {0}".format(train_x.shape))
    print("Training Label Shape: {0}".format(train_y.shape))
    print("Test Features Shape: {0}".format(test_x.shape))
    print("Test Label Shape: {0}".format(test_y.shape))


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
