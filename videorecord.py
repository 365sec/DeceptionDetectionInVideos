import cv2
from tkinter.filedialog import *

def videorecord():
    path_ = asksaveasfilename(defaultextension='.mp4', title='选择保存的位置', filetypes=[('视频文件', '.mp4')])
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(1, 10.0)
    fourcc1 = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # 第三个参数则是镜头快慢的，10为正常，小于10为慢镜头
    out = cv2.VideoWriter(path_, fourcc1, 10, (640, 480))
    while True:
        ret, frame = cap.read()
        if ret is True:
            frame = cv2.flip(frame, 1)
            out.write(frame)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
