# coding: utf-8

import sys
from enum import IntEnum
import numpy as np
from sklearn.svm import SVC

works = IntEnum("Works", ["?", "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"])
education = IntEnum("Education Level", ["?", "Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"])
marriage = IntEnum("Marriage", ["?", "Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"])
occupation = IntEnum("Occupation", ["?", "Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"])
home_role = IntEnum("Home Role", ["?", "Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"])
race = IntEnum("Race", ["?", "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"])
gender = IntEnum("Gender", ["?", "Female", "Male"])
nationality = IntEnum("Nationality", ["?", "United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany", "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador", "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands"])

def people2arr(s):
    k = [x.strip() for x in s.split(",")]
    arr = [0]*13
    arr[0] = int(k[0])
    arr[1] = works[k[1]].value
    arr[2] = education[k[2]].value
    arr[3] = marriage[k[3]].value
    arr[4] = occupation[k[4]].value
    arr[5] = home_role[k[5]].value
    arr[6] = race[k[6]].value
    arr[7] = gender[k[7]].value
    arr[8] = int(k[8])
    arr[9] = int(k[9])
    arr[10] = int(k[10])
    try:
        arr[11] = nationality[k[11]].value
    except KeyError:
        print k
        print k[11]
        raise

    if len(k) == 13:
        return arr, int(k[12])
    else:
        return arr, None

clf = SVC(gamma=0.001, C=100.)
training_data = []
training_result = []

with file("adult.txt") as f:
    for line in f:
        d, r = people2arr(line)
        training_data.append(d)
        training_result.append(r)

print "Training Dataset Get"

clf.fit(np.array(training_data), training_result)
print "Learning finished"

p_d = []
final = []
with file("adult_test.txt") as f:
    for line in f:
        d, _ = people2arr(line)
        p_d.append(d)

print "Predicting Dataset Get"

final = clf.predict(p_d)
with file("final_result.txt", "w") as f:
    f.write("".join([str(x) for x in final]))
print final

print "Done"
