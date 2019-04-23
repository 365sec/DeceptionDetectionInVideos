Train.py
import numpy as np
import pandas as pd
import sklearn
import cv2
import os
rootdir = 'jaffe'
desdir = 'jaffe_resize'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
for file_name in os.listdir(rootdir):
    if file_name[-4:] == 'tiff':
        img = cv2.imread(rootdir+'/'+file_name)
        faces = face_cascade.detectMultiScale(img, 1.1, 5)
        x, y, h, w = faces[0][0], faces[0][1], faces[0][2], faces[0][3]
        img_f = img[y:y+h, x:x+w]
        img_resize = cv2.resize(img_f, (255, 255))
        cv2.imwrite(desdir+'/'+file_name, img_resize) x = []
y = []
rootdir = 'jaffe_resize'
for file_name in os.listdir(rootdir):
    if file_name[-4:] == 'tiff':
        tmp = cv2.imread(rootdir+'/'+file_name)
        tmp = tmp.flatten()
        tmp = tmp.tolist()
        x.append(tmp)
        y.append(file_name[3:5])
x = np.array(x)
y = np.array(y)
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=33)
from sklearn.svm import SVC
svc_linear = SVC(kernel='linear',probability=True)
svc_linear.fit(x_train, y_train)
svc_linear.predict(x_test)
from sklearn.svm import SVC
svc_linear = SVC(kernel='linear',probability=True)
svc_linear.fit(x, y)
from sklearn.externals import joblib
joblib.dump(svc_linear, 'detection.m')
