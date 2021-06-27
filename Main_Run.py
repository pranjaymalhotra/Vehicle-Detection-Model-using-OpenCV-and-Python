import os
import webbrowser
#import number_plate
#import VD_camera
#import VD_Local_video
print("Hello! user choose your tool")
while True:
    print("Choose your tool :-\n")
    print("1.Start VEHICLE Counting")
    print("2.Start Number Plate Recognition")
    print("3.Run NotePad")
    print("4.Check Vehicle Details And License Details")
    print("5.Exit")
    p = int(input())
    if(p!=1 or p!=2 or p!=3):
        if(p==1):
            exec(open('VD_camera.py').read())
        elif(p==2):
            exec(open('number_plate.py').read())
        elif(p==3):
            os.system("C:\\Windows\\notepad.exe")
        elif (p==4):
            webbrowser.open("https://parivahan.gov.in/parivahan//en/node/2632")
        elif(p==5):
            break
        else:
            print("INVALID Entry")


