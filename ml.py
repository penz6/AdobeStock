from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report


#load adobe data set
df = pd.read_csv('Training.csv')

#split the tags up into an array of numpy as thats what works with sklearn,
#not a standard python array
#df['title'] = df["title"].str.split(" ")
#df['title'] = np.array(df['title'])
df['is_premium'] = df['is_premium'].replace(['True'], True)
df['is_premium'] = df['is_premium'].replace(['False'], False)
#linear encode
le = LabelEncoder()
df['title_encoded'] = le.fit_transform(df['title'])
#df['title'] = pd.get_dummies(df['title'])
print(df['title'])
print(df['title_encoded'])
print(list(le.classes_))

X_train, X_test, y_train, y_test = train_test_split(df[['title_encoded']], df['premium_level_id'], test_size=.3)
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)
# Test the classifier by giving it test instances
prediction = classifier.predict(X_test)
# Count how many were correctly classified
correct = np.where(prediction==y_test, 1, 0).sum()
print(correct)
# Calculate the accuracy of this classifier
accuracy = correct/len(y_test)
print(accuracy)
print(prediction)
#mean error squared
print(mean_squared_error(y_test, prediction))
# graph
encode = sns.histplot(data=df, x='title_encoded')
encode.set(title='Encoded Distribution',xlabel="Title Encoded Value")
plt.show()


ispremium = sns.histplot(data=df, x='is_premium')
ispremium.set(title='Premium vs Non Premium Assets',xlabel="Is a Premium Asset",xlim=[0,1])
plt.show()

premlev = sns.histplot(data=df, x='premium_level_id')
premlev.set(title='Premium Level Distribution',xlabel="Premium Level Value")
plt.show()
#sklearn graph built in
print(classification_report(y_test, prediction))
