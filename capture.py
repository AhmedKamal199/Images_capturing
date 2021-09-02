import cv2 as cv


cam = cv.VideoCapture(0, cv.CAP_DSHOW) #captureDevice = camera

cv.namedWindow("Test")

img_c = 0
while True:
    ret,frame = cam.read()
    if not ret:
        print("Error")
        break
    cv.imshow("image", frame)
    k = cv.waitKey(1)

    if cv .waitKey(1) & 0xFF == ord('q'):
        break

    elif k % 256 == 32:
        cv.imwrite("out.png", frame)
        print("done")
        img_c+=1

cam.release()

cv.destroyAllWindows()