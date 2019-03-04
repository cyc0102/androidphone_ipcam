
import cv2


# url= "http://192.168.169.169:8080/shot.jpg"
stream = cv2.VideoCapture('http://192.168.169.169:8080/video')

while True:
    r, f = stream.read()
    cv2.imshow('IP Camera stream',f)

    if cv2.waitKey(1) == 27:   # Press esc to exit
        break

cv2.destroyAllWindows()
