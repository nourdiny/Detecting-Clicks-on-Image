import cv2
import numpy as np

# Set image dimensions
wImg = 450
hImg = 550

# Initialize circles and counter
circles = np.zeros((4, 2), dtype=int)
counter = 0

# Mouse click callback function
def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN and counter < 4:
        circles[counter] = (x, y)
        counter += 1

# Load and resize the image
img = cv2.imread("img/img.jpg")
img = cv2.resize(img, (wImg, hImg))

while True:
    if counter == 4:
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [wImg, 0], [0, hImg], [wImg, hImg]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgWarp = cv2.warpPerspective(img, matrix, (wImg, hImg))
        cv2.imshow("Warped img", imgWarp)
        counter = 0
        circles = np.zeros((4, 2), dtype=int)

    for x in range(0, 4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 4, (0, 255, 0), cv2.FILLED)

    cv2.imshow("img", img)
    cv2.setMouseCallback("img", mousePoints)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
