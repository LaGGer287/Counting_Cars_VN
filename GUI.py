import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import cvzone
from tracker import *
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

model = YOLO('best2.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    my_file = open("a.txt", "r")
    data = my_file.read()
    class_list = data.split("\n")

    count = 0
    tracker = Tracker()
    tracker2 = Tracker()
    tracker3 = Tracker()

    area1 = [(240, 361), (178, 435), (680, 435), (630, 361)]
    area_1 = set()
    area_2 = set()
    area_3 = set()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        count += 1
        if count % 3 != 0:
            continue
        frame = cv2.resize(frame, (1020, 500))
        results = model.predict(frame)
        a = results[0].boxes.data
        px = pd.DataFrame(a).astype("float")
        list = []
        list2 = []
        list3 = []
        for index, row in px.iterrows():
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            d = int(row[5])
            c = class_list[d]
            if 'Oto' in c:
                list.append([x1, y1, x2, y2])
                cv2.putText(frame,str(c),(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2 )
                #cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            elif 'XeMay' in c:
                list2.append([x1, y1, x2, y2])
                cv2.putText(frame,str(c),(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2 )
                #cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            elif 'XeCont' in c:
                list3.append([x1, y1, x2, y2])
                cv2.putText(frame,str(c),(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2 )
                #cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        bbox_idx = tracker.update(list)
        bbox_idx2 = tracker2.update(list2)
        bbox_idx3 = tracker3.update(list3)

        for bbox in bbox_idx:
            x3, y3, x4, y4, id = bbox
            cx = int(x3 + x4) // 2
            cy = int(y3 + y4) // 2
            result = cv2.pointPolygonTest(np.array(area1, np.int32), ((cx, cy)), False)
            if result >= 0:
                area_1.add(id) 
            
        for bbox2 in bbox_idx2:
            x5, y5, x6, y6, id2 = bbox2
            cx2 = int(x5 + x6) // 2
            cy2 = int(y5 + y6) // 2
            result2 = cv2.pointPolygonTest(np.array(area1, np.int32), ((cx2, cy2)), False)
            if result2 >= 0:
                area_2.add(id2)
            
        for bbox3 in bbox_idx3:
            x7, y7, x8, y8, id3 = bbox3
            cx3 = int(x7 + x8) // 2
            cy3 = int(y7 + y8) // 2
            result3 = cv2.pointPolygonTest(np.array(area1, np.int32), ((cx3, cy3)), False)
            if result3 >= 0:
                area_3.add(id3)
      
        a = len(area_1)
        b = len(area_2)
        e = len(area_3)

        cv2.putText(frame,"So luong xe o to: " + str(a),(65,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2 )
        cv2.putText(frame,"So luong xe may " + str(b),(65,85),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2 )
        cv2.putText(frame,"So luong xe container: " + str(e),(65,110),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2 )
        #cvzone.putTextRect(frame, f'So o to: {a}', (50, 60), 1, 1)
        #cvzone.putTextRect(frame, f'So xe may: {b}', (50, 80), 1, 1)
        #cvzone.putTextRect(frame, f'So xe container: {e}', (50, 100), 1, 1)

        cv2.polylines(frame, [np.array(area1, np.int32)], True, (255, 255, 0), 2)
        cv2.imshow("He thong dem luu luong phuong tien giao thong", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    print("Final Results:") 
    print(f'So o to: {a}')
    print(f'So xe may: {b}')
    print(f'So xe container: {e}')

    output_file_path_final = os.path.abspath("output_final.txt")
    with open(output_file_path_final, "w") as file:
        file.write("Final Results:\n")
        file.write(f'So o to: {a}\n')
        file.write(f'So xe may: {b}\n')
        file.write(f'So xe container: {e}\n')

    print("Kết quả được in ở:", output_file_path_final)
    
    cap.release()
    cv2.destroyAllWindows()

###################################################################################################################
def open_output_final_txt():
    os.system("notepad output_final.txt")
    
def exit_app():
    root.destroy()

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
    if file_path:
        process_video(file_path)

root = tk.Tk()
root.title("Hệ thống đếm lưu lượng phương tiện giao thông")

label_program = tk.Label(root, text="Hệ thống đếm lưu lượng phương tiện giao thông", font=("Helvetica", 20), bg="#FFFF00", fg="black")
label_program.pack(fill=tk.X)

button_choose_video = tk.Button(root, text="Chọn Video", command=choose_file, bg="#3498db", fg="white", font=("Helvetica", 12))
button_choose_video.place(relx = 0.12, rely=0.30,anchor="center")

button_open_output_final_txt = tk.Button(root, text="Kết quả", command=open_output_final_txt,bg="#2ecc71", fg="white", font=("Helvetica", 12))
button_open_output_final_txt.place(relx = 0.1, rely=0.45,anchor="center")

button_exit = tk.Button(root, text="Thoát", command=exit_app, bg="#e74c3c", fg="white", font=("Helvetica", 12))
button_exit.place(relx= 0.9, rely=0.9, anchor="center")
root.geometry("600x350")

image = Image.open('E:/KI_7/TGMT/1.jpg')
image2 = image.resize((400,200))
image3 = ImageTk.PhotoImage(image2)
label2 = tk.Label(image=image3).place(relx = 0.55, rely= 0.53, anchor="center")

root.mainloop()
