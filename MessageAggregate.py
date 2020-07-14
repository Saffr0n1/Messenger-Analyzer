# Abishrant Panday 2020
# Allows users to automatically upload all html files in a given folder for easier analysis

import TextParser
import glob

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

    return len(bigList)