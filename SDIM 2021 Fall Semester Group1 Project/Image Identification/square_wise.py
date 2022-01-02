from sklearn.svm import LinearSVC
import cv2
import os
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def test():
    model = LinearSVC(C=1e-2)
    model = joblib.load("SVM-modelv0.m")
    y = openreadtxt("Photo-cut/label.txt")
    y = np.asarray(y)
    path = "photo/"
    f = os.listdir(path)
    width = 95
    height = 95
    now = -1
    k = 0
    filename = f[k]
    imgs = []
    img = cv2.imread(path + filename)
    for i in range(3):
        for j in range(4):
            imgnow = img[i * height: (i + 3) * height, 50 + j * width: 50 + (j + 3) * width]
            imgnow = cv2.resize(imgnow, (95, 95))
            imgs.append(imgnow)
    imgs = np.asarray(imgs)
    imgs = np.reshape(imgs, (imgs.shape[0], -1))
    y_pre = model.predict(imgs)
    plt.imshow(img)
    print(y_pre)
    print(y[k * 12:(k + 1) * 12])
    plt.show()


def openreadtxt(file_name):
    data = []
    file = open(file_name, 'r')
    file_data = file.readlines()
    for row in file_data:
        now = []
        tmp_list = row.split('\t')
        tmp_list[-1] = tmp_list[-1].replace('\n', ',')
        for item in tmp_list:
            now.append(int(item[0]))
        data = data + now
    return data


from sklearn.metrics import accuracy_score, precision_score, recall_score


path = "Photo-cut/"
f = os.listdir(path)
now = -1
imgs = []
imgs = np.asarray(imgs)
y = openreadtxt("Photo-cut/label.txt")
y = np.asarray(y)
imgs = np.reshape(imgs, (imgs.shape[0], -1))
imgs = imgs
y = y

# scaler = StandardScaler()
# imgs = scaler.fit_transform(imgs)
x_train, x_test, y_train, y_test = train_test_split(imgs, y, test_size=0.2, random_state=7)
'''

model.fit(x_train, y_train)
joblib.dump(model, "SVM-modelv0.m")
pre_y = model.predict(x_train)
print(model.score(x_train, y_train))
print(accuracy_score(pre_y, y_train))
print(precision_score(pre_y, y_train))
print(recall_score(pre_y, y_train))

'''

model = joblib.load("SVM-modelv0.m")
# 预测,test为测试集
print("test")
pre_y = model.predict(x_test)
#pre_y = np.random.randint(0, 2, size=(x_test.shape[0]))
print(accuracy_score(pre_y, y_test))
print(precision_score(pre_y, y_test))
print(recall_score(pre_y, y_test))
# test()
