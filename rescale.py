from turtle import width
import cv2 as cv

# img = cv.imread("images/dog.24.jpg")
# cv.imshow("dog",img)
def rescaleImages(frame,scale = 1):
    width =frame.shape[1] * scale
    height = frame.shape[0] * scale

    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
# cv.waitKey(0)
capture = cv.VideoCapture("videos\pexels-marc-espejo-6548176.mp4")
while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleImages(frame)


    cv.imshow("Video",frame)
    cv.imshow("Video Resized",frame_resized)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break
capture.release()
cv.destroyAllWindows()
