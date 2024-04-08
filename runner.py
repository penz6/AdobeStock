import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

from api import api
import pandas as pd


def main():
    print("hello")
    # example traning query
    data = api("dogs")
    print(data)
    #get data into data frame
    df = pd.json_normalize(data['files'],max_level=0)
    print(df)
    # save data to file
    pd.DataFrame.to_csv(df,"Traning")



#call main
main()