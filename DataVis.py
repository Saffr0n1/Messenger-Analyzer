# Abishrant Panday 2020
# General helper file that contains many useful seaborn data visualization functions
# Allows viewing relationships in Messenger data visually

import MessageAggregate

i = MessageAggregate.aggregator("Data/")
print(len(i))


def time_frequency(inputList, scale):
    if (scale == "Month"):

