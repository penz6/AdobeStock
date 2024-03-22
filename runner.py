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
    #train/test data
    X_train, X_test, y_train, y_test = train_test_split(df[['premium_level_id']], df['title'], test_size=.2)
    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(X_train, y_train)
    prediction = classifier.predict(X_test)
    # Count how many were correctly classified
    correct = np.where(prediction==y_test, 1, 0).sum()
    print(correct)
    # Calculate the accuracy of this classifier
    accuracy = correct/len(y_test)
    print(accuracy)



#call main
main()