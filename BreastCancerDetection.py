# -*- coding: utf-8 -*-
"""BreastCancerDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TJiohT6_J3Yh1DFy8-0jDYX2yFoCaKtR

Let’s start by importing and loading the necessary python libraries and the breast cancer dataset provided by Scikit-learn
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

"""Now we need to create new variables for each important set of information that we find useful and assign the attributes in the dataset to those variables:"""

data = load_breast_cancer()
label_names = data["target_names"]
labels = data["target"]
feature_names = data["feature_names"]
features = data["data"]

"""We now have values for each set of useful information in the dataset. To better understand our dataset, let’s take a look at our data by printing our class labels, the label for the first data instance, our entity names, and the entity values for the first data instance"""

print(label_names)
print("Class label :", labels[0])
print(feature_names)
print(features[0], "\n")

"""To evaluate the performance of a classifier, you should always test the model on invisible data. Therefore, before I create a machine learning model for breast cancer detection, I will divide your data into two parts: an 80% training set and a 20% test set:"""

train, test, train_labels, test_labels = train_test_split(features, labels,
                                                          test_size=0.2,
                                                          random_state=42)

"""For the Breast Cancer Detection Model task, I will focus on a simple algorithm that generally works well in binary classification tasks, namely the Naive Bayes classifier"""

gnb = GaussianNB()
gnb.fit(train, train_labels)

"""The predict() function returns an array of predictions for each data instance in the test set. We can then print out our predictions to get a feel for what the model determined"""

preds = gnb.predict(test)
print(preds, "\n")

"""Using the array of true class labels, we can assess the accuracy of our model’s predictors by comparing the two arrays (test_labels vs preds).

I’ll use the accuracy_score () function provided by Scikit-Learn to determine the accuracy rate of our machine learning classifier
"""

print(accuracy_score(test_labels, preds))

"""As you can see from the output above, our breast cancer detection model gives an accuracy rate of almost 97%. This means that 97% of the time the classifier is able to make the correct prediction"""
