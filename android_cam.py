import requests
import cv2
import numpy as np

url= "http://192.168.169.169:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1) # -1 CV_LOAD_IMAGE_UNCHANGED
    cv2.imshow('AndroidCam',img)

    if cv2.waitKey(1) == 27:   # Press esc to exit
        break
