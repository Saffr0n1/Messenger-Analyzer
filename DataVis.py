# Abishrant Panday 2020
# General helper file that contains many useful data visualization functions
# Allows viewing relationships in Messenger data visually

import MessageAggregate
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

i = MessageAggregate.aggregator("Data/")
print(i.groupby(i.index.day)['Name'].value_counts())
print(i['Name'].value_counts())


def time_frequency(inputList, scale, startRange, endRange, color):
    if startRange == 'Beginning':
        startRange = inputList.index[1]
    if endRange == 'End':
        endRange = inputList.index[-1]

    inputList = inputList.loc[startRange:endRange]

    if (scale == "Default"):
        sns.set(rc={'figure.figsize': (18, 4)})
        inputList["Date"] = inputList.index.round('1d').date
        il2 = inputList.groupby('Date').agg({'Name': 'value_counts'})
        reindex(il2,color,"Date")

    if (scale == "Year"):
        sns.set(rc={'figure.figsize': (4, 4)})
        il2 = inputList.groupby('Year').agg({'Name': 'value_counts'})
        reindex(il2,color,"Year")

    if (scale == "Month"):
        sns.set(rc={'figure.figsize': (4, 4)})
        il2 = inputList.groupby('Month').agg({'Name': 'value_counts'})
        reindex(il2,color,"Month")

    if (scale == "Day"):
        sns.set(rc={'figure.figsize': (4, 4)})
        il2 = inputList.groupby('Weekday').agg({'Name': 'value_counts'})
        reindex(il2,color,"Weekday")


def reindex(inputList, color,index):
    inputList.columns = ['Frequencies']
    pivot = pd.pivot_table(inputList.reset_index(), values='Frequencies', index=index, columns='Name').fillna(0)
    ax = pivot.plot(kind='bar', stacked=True, color=color)
    ax.set_xticklabels(labels=pivot.index, rotation=70, rotation_mode="anchor", ha="right")
    ax.set_ylabel("Number of Messages")
    ax.set_xlabel(index)
    plt.legend()
    plt.show()

# def all_frequency(inputList, startRange, endRange):
#     if startRange == 'Beginning':
#         startRange = inputList.index[1]
#     if endRange == 'End':
#         endRange = inputList.index[-1]
#
#     inputList = inputList.loc[startRange:endRange]













