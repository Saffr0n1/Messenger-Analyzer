# Abishrant Panday 2020
# Allows users to automatically upload all html files in a given folder for easier analysis
import numpy

import TextParser
import glob
import pandas as pd

# path_to_dir is the path to the folder containing html messages
def aggregator(path_to_dir):
    files = glob.glob(path_to_dir + '/*.html', recursive=True)
    bigList = []
    for file in files:
        s = TextParser.text_to_string(file)
        f = TextParser.text_filter(s)
        c = TextParser.cleanse(f)
        for item in c:
            bigList.append(item)

    listDF = pd.DataFrame(bigList, columns=['Name', 'Message', 'Date Time'])
    listDF['Date Time'] = pd.to_datetime(listDF['Date Time'])
    listDF = listDF.set_index('Date Time')
    listDF['Year'] = listDF.index.year
    listDF['Month'] = listDF.index.month
    listDF['Day'] = listDF.index.day
    listDF['Time'] = listDF.index.time
    listDF['Weekday'] = listDF.index.day_name()
    return listDF


