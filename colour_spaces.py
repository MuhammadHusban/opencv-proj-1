import cv2 as cv

img = cv.imread('images\dog.32.jpg')
cv.imshow('dog', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

# Lab to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
# cv.imshow('LAB --> BGR', lab_bgr)


# gray to BGR
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
# cv.imshow('gray --> BGR', gray_bgr)

cv.waitKey(0)