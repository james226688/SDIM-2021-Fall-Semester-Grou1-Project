from sklearn.svm import LinearSVC, NuSVC, SVC
import cv2
import os
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, roc_curve, auc


def test():
    model = LinearSVC()
    model = joblib.load("SVM-modelv0.m")
    # y = openreadtxt("Photo-point/label.txt")
    # y = np.asarray(y)
    path = "photo/"
    f = os.listdir(path)
    width = 95
    height = 95
    now = -1
    k = 30
    filename = f[k]
    imgs = []
    B = cv2.imread(path + filename)[..., 0][..., None]
    G = cv2.imread(path + filename)[..., 1][..., None]
    R = cv2.imread(path + filename)[..., 2][..., None]
    img2show = np.concatenate((R, G, B), axis=-1)
    img = cv2.imread(path + filename)
    for i in range(3):
        for j in range(4):
            imgnow = img[i * height: (i + 3) * height, 50 + j * width: 50 + (j + 3) * width]
            imgnow = cv2.resize(imgnow, (27, 27))
            imgs.append(imgnow)
    imgs = np.asarray(imgs).reshape(12, -1)
    y_pre = model.predict(imgs)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # mask = np.zeros_like(img)
    plt.imshow(img2show)
    rec = plt.Rectangle((40 + 2 * width, 3 * height - 20), width, height, color='yellow', alpha=0.5)
    ax.add_patch(rec)
    rec = plt.Rectangle((40 + 0 * width, 2 * height - 20), width, height, color='yellow', alpha=0.5)
    ax.add_patch(rec)
    rec = plt.Rectangle((40 + 1 * width, 2 * height - 20), width, height, color='yellow', alpha=0.5)
    ax.add_patch(rec)
    rec = plt.Rectangle((40 + 4 * width, 1 * height - 20), width, height, color='red', alpha=0.5)
    ax.add_patch(rec)
    plt.show()
    print(y_pre)


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



model = SVC(kernel='sigmoid', C=1e5)
# model = KNeighborsClassifier(n_neighbors=5)
# model = DecisionTreeClassifier()
# model = MultinomialNB(alpha=1.0)
path = "Photo-point/"
f = os.listdir(path)
now = -1
imgs = []
for filename in f:
    now = now + 1
    imgnow = cv2.imread(path + filename)
    #imgnow = cv2.resize(imgnow, (95, 95))
    plt.imshow(imgnow)
    imgs.append(imgnow)
    if now == 79 * 12 - 1:
        break
imgs1 = []
imgs2 = []
imgs3 = []
for image in imgs:
    img1 = cv2.flip(image, 0)
    img2 = cv2.flip(image, 1)
    img3 = cv2.flip(image, -1)
    imgs1.append(img1)
    imgs2.append(img2)
    imgs3.append(img3)

imgs = np.asarray(imgs)
imgs1 = np.asarray(imgs1)
imgs2 = np.asarray(imgs2)
imgs3 = np.asarray(imgs3)
imgs = np.concatenate((imgs, imgs1, imgs2, imgs3), axis=0)
y = openreadtxt("Photo-cut/label.txt")
y = np.asarray(y)
y = np.concatenate((y, y, y, y), axis=0)

imgs = np.reshape(imgs, (imgs.shape[0], -1))
imgs = imgs
y = y

# scaler = StandardScaler()
# imgs = scaler.fit_transform(imgs)
x_train, x_test, y_train, y_test = train_test_split(imgs, y, test_size=0.2, random_state=7)
'''

'''
model.fit(x_train, y_train)
joblib.dump(model, "my_model_point.m")
pre_y = model.predict(x_train)
print(model.score(x_train, y_train))
print(accuracy_score(pre_y, y_train))
print(precision_score(pre_y, y_train))
print(recall_score(pre_y, y_train))

model = joblib.load("my_model_point.m")
# 预测,test为测试集
print("test")
pre_y = model.predict(x_test)
# pre_y = np.random.randint(0, 2, size=(x_test.shape[0]))
print(accuracy_score(pre_y, y_test))
print(precision_score(pre_y, y_test))
print(recall_score(pre_y, y_test))


test()
