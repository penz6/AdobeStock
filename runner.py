import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

from api import api
import pandas as pd


def main():
    print("hello")
    #data frame
    df = pd.DataFrame()
    #get both premium and non premium
    premium_list = ['true','false']
    #animal list
    search_list = ['true','false']
    for premium in premium_list:
        for
        # offset
        for i in range(0,5000,100):
            data = api("dogs",i,premium)
            print(data)
            #get data into data frame
            dftemp = pd.json_normalize(data['files'],max_level=0)
            df = pd.concat([df,dftemp])
    # save data to file
    pd.DataFrame.to_csv(df,"Training.csv")



#call main
main()