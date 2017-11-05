#! python3
__author__ = "Rajesh Pachaikani"
__copyright__ = "None"
__credits__ = ["Opencv Developers"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Author"
__email__ = "rajeshpachaikani@gmail.com"
__status__ = "Release"


import cv2
import numpy as np

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
rec = cv2.VideoWriter("output.avi", fourcc,17 , (640, 480))
flag = False
font = cv2.FONT_HERSHEY_SIMPLEX

while 1:
    b, img = cam.read()
    if b:
        cv2.putText(img,"c-Capture  s-Save  q- Quit",(100,50),cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,color=(100,100,100), thickness=3)

    key = cv2.waitKey(1) & 0XFF
    if key == ord('c'):
        flag = True

    if flag:
        cv2.putText(img, "Recording", (50, 100), cv2.FONT_HERSHEY_PLAIN, fontScale=2,
                    color=(100, 100, 100))
        rec.write(img)

    if key == ord('s'):
        flag = False

    if not flag:
        rec.release()

    if key == ord('q'):
        rec.release()
        break
    cv2.imshow("ViewPort", img)

cv2.destroyAllWindows()
