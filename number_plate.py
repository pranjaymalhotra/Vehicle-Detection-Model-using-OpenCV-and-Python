import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pyperclip
pytesseract.pytesseract.tesseract_cmd = 'C:/Tesseract-OCR/tesseract.exe'
print("Select ->")
print("1.Start With Stock Image")
print("2.Start With Custom Image")
x=int(input())
if (x == 1):
        img = cv2.imread('2.jpg',cv2.IMREAD_COLOR)
elif (x == 2):
        Tk().withdraw()
        img2 = askopenfilename()
        img = cv2.imread(img2, cv2.IMREAD_COLOR)
else:
        print("INVALID ENTRY")
img = imutils.resize(img, width=500 )
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1=img.copy()
cv2.drawContours(img1,cnts,-1,(0,255,0),3)
cv2.imshow("img1",img1)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
screenCnt = None
img2 = img.copy()
cv2.drawContours(img2,cnts,-1,(0,255,0),3) 
cv2.imshow("img2",img2)

count=0
idx=7
for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        if len(approx) == 4:
                screenCnt = approx
                x,y,w,h = cv2.boundingRect(c)
                new_img=img[y:y+h,x:x+w]
                cv2.imwrite('./'+str(idx)+'.png',new_img)
                idx+=1
                break
cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("Final image with plate detected",img)

Cropped_loc='./7.png'
cv2.imshow("cropped",cv2.imread(Cropped_loc))
pytesseract.pytesseract.tesseract_cmd=r"C:/Tesseract-OCR/tesseract.exe"

text=pytesseract.image_to_string(Cropped_loc,lang='eng')
print("Number is:" ,text)
print("Vehicle Number Copied To Clipboard")
pyperclip.copy(text)
if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows() 
