from tkinter.filedialog import *
import cv2
import numpy as np
from sklearn.externals import joblib
svc_linear = joblib.load('detection.m')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

def predict(predict_value):
    path_ = askopenfilename(title='选择要预测的视频', filetypes=[('视频文件', '.mp4')])
    vc = cv2.VideoCapture(path_)
    c = 1
    rval, frame = vc.read()
    timeF = 15
    res = []
    while rval:
        rval, frame = vc.read()
        if (c % timeF == 0):
            res.append(detection(frame))
        c += 1
        cv2.waitKey(1)
    vc.release()
    result = max(res)
    predict_value.set(result)#这里是设置预测结果的

    '''
    cap = cv2.VideoCapture(path_)
    rval, frame = cap.read()
    timeF = 1
    while rval:
        ret, frame = cap.read()
        if (c % timeF == 0):
            cv2.imshow(path_, frame)
        else:
            break
        c += 1
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()
    '''


def detection(img):
    faces = face_cascade.detectMultiScale(img, 1.1, 5)
    if len(faces) == 1:
        x, y, h, w = faces[0][0], faces[0][1], faces[0][2], faces[0][3]
        img_f = img[y:y+h, x:x+w]
        img_resize = cv2.resize(img_f, (255, 255))
        x = img_resize.reshape(1, -1)
        expression = svc_linear.predict_proba(x)[0]
        prob = [0.2, 0.4, 0.6, 0.2, -0.2, 0.2, 0.4]
        detection_prob = 0
        for i in range(0, len(prob)):
            detection_prob += expression[i] *prob[i]
        return detection_prob
    return 0