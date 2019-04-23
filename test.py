from predict import *
from videorecord import *
from tkinter import *

root = Tk()
predict_value = StringVar()
root.wm_geometry('600x300+100+50')
root.title("测谎系统")
frame2 = Frame(root, height=60, width=30)#用于放按钮和文本框

label = Label(frame2, text="说谎概率：")
label.pack(fill=X, padx=10, pady=10)
entry = Entry(frame2, textvariable=predict_value)
entry.pack(fill=X, padx=10, pady=10)
button1 = Button(frame2, text="开始录像", command=lambda: videorecord())
button1.pack(fill=X, padx=10, pady=10)
#button2 = Button(frame2, text="停止录像")
#button2.pack(fill=X, padx=10, pady=10)
button3 = Button(frame2, text="选择录像", command=lambda: predict(predict_value))
button3.pack(fill=X, padx=10, pady=10)


frame2.pack()
root.mainloop()

