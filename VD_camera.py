import cv2
import numpy as np
from time import sleep
from tkinter import Tk
from tkinter.filedialog import askopenfilename
W_min=80
H_min=80

offset=6
pos_line=550

delay= 60

detect = []
car= 0

def get_center(x, y, w, h):
        x1 = int(w / 2)
        y1 = int(h / 2)
        cx = x + x1
        cy = y + y1
        return cx,cy
print("Select ->")
print("1.Video Input from camera")
print("2.Video Input from Local Storage")
x=int(input())
if(x==1):
    vid = cv2.VideoCapture(0)
elif(x==2):
    Tk().withdraw()
    vid2 = askopenfilename()
    vid = cv2.VideoCapture(vid2)
else:
    print("INVALID ENTRY")
subtract = cv2.bgsegm.createBackgroundSubtractorMOG()
while True:
    ret , frame1 = vid.read()
    tempo = float(1/delay)
    sleep(tempo) 
    grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),5)
    img_sub = subtract.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
    dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    contorno,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.line(frame1, (25, pos_line), (1200, pos_line), (255,127,0), 3)
    for(i,c) in enumerate(contorno):
        (x,y,w,h) = cv2.boundingRect(c)
        validate_outline = (w >= W_min) and (h >= H_min)
        if not validate_outline:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
        center = get_center(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0,255), -1)

        for (x,y) in detect:
            if y<(pos_line+offset) and y>(pos_line-offset):
                car+=1
                cv2.line(frame1, (25, pos_line), (1200, pos_line), (0,127,255), 3)
                detect.remove((x,y))
                print("car is detected : "+str(car))
       
    cv2.putText(frame1, "VEHICLE COUNT : "+str(car), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
    cv2.imshow("Video Original" , frame1)
    cv2.imshow("Detectar",dilatada)

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
vid.release()
