# Abishrant Panday 2020
# Takes a message.html file from Facebook and returns all text messages
# Messages that are links, images, stickers, etc. will not be returned
# Utilizes common patterns found within the structure of each message.html file
# For each message, the sender and the time sent are attached as well

import re


def text_to_string(file):
    rawMessage = open(file, 'r', encoding="utf8")
    rawString = rawMessage.read()
    return rawString


def text_filter(string):
    coarseFilter = "<div class=\"pam _3-95 _2pi0 _2lej uiBoxWhite noborder\"><div class=\"_3-96 _2pio _2lek _2lel\">" \
                   "[a-zA-Z0-9_,;'\"\s.?!]+<\/div><div class=\"_3-96 _2let\"><div><div><\/div><div>[a-zA-Z0-9_,:;'’\"\s.?!(&#039;)]" \
                   "+<\/div><div><\/div><div><\/div><\/div><\/div><div class=\"_3-94 _2lem\">[a-zA-Z0-9_,;:'\"\s.?!]+<\/div><\/div>";
    rawText = re.findall(coarseFilter, string)
    senderFilter =
    messageFilter =
    timeFilter =
    return len(rawText)


print(text_filter(text_to_string("Data\message_1.html")))
#     for i in range(len(rawText)):
#         rawText[i] = rawText[i][16:-28]