#
# Copyright (c) 2017 ElementAI. All rights reserved.
#
import os
import pandas as pd
from sklearn.model_selection import train_test_split

dataset_filename = os.getenv('DATASET_FILENAME')
test_size = float(os.getenv('TEST_SIZE'))
dir_path = os.path.dirname(os.path.realpath(__file__))

print("Loading {}".format(dataset_filename))
dataset = pd.read_csv(dir_path + '/../input/' + dataset_filename, header=None, sep=',')

train, test = train_test_split(dataset, test_size=test_size)
train.to_csv(dir_path + '/../output/training_' + dataset_filename)
test.to_csv(dir_path + '/../output/testing_' + dataset_filename)
