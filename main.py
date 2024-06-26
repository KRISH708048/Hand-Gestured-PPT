import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# dimensional and  path variable
width, height = 1280, 720
presentationFolderPath = f"Presentations/"
pathImages = sorted(os.listdir(presentationFolderPath), key=len)
slideNo = 0
sh, sw = 120, 213

# Setting camera
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# gesture variables
detector = HandDetector(detectionCon=0.8, maxHands=1)
gestureDetectThreshold = 450
buttonPressed = False
buttonPressedCount = 0
buttonDelay = 20
xVal, yVal = 0, 0
fingersUp = []
indexFinger = 2
annotations = [[]]
annotInd = -1
annotSet = False

while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)
    cv2.line(img, (0, gestureDetectThreshold), (width, gestureDetectThreshold), (0, 255, 0), 4)
    fullPath = os.path.join(presentationFolderPath, pathImages[slideNo])
    currentImg = cv2.imread(fullPath)
    currentImg = cv2.resize(currentImg, (width, height))
    sideImg = cv2.resize(img, (sw, sh))
    currentImg[0:sh, width - sw:width] = sideImg
    hands, img = detector.findHands(img)

    if hands and buttonPressed is False:
        hand = hands[0]
        fingersUp = detector.fingersUp(hand)
        # print(fingersUp)
        cx, cy = hand['center']
        lmList = hand['lmList']
        indexFinger = lmList[8][0], lmList[8][1]
        xVal = indexFinger[0]
        yVal = indexFinger[1]
        indexFinger = int(np.interp(indexFinger[0], [width//2, width], [0, width])), int(np.interp(indexFinger[1]
                                                                                    , [100, height-100], [0, height]))
        if cy <= gestureDetectThreshold:    # gesture- left slide
            if fingersUp == [1, 0, 0, 0, 0]:
                # print("left")
                buttonPressed = True
                annotations = [[]]
                annotSet = False
                annotInd = -1
                if slideNo > 0:
                    slideNo -= 1
            if fingersUp == [0, 0, 0, 0, 1]:    # gesture- right slide
                # print("left")
                buttonPressed = True
                annotations = [[]]
                annotInd = -1
                annotSet = False
                if slideNo < len(pathImages) - 1:
                    slideNo += 1

        if fingersUp == [0, 1, 0, 0, 0]:
            cv2.circle(currentImg, (indexFinger[0], indexFinger[1]), 10, (0, 0, 255), cv2.FILLED)
            if not annotSet:
                annotSet = True
                annotInd += 1
                annotations.append([])
            annotations[annotInd].append(indexFinger)
        else:
            annotSet = False

        if fingersUp == [0, 1, 1, 1, 0]:
            if annotations:
                annotations.pop(-1)
                annotInd -= 1
                annotSet = False
                buttonPressed = True

        if fingersUp == [0, 1, 1, 0, 0] and xVal >= width // 2:   # gesture- pointer over slide
            # print(xVal, yVal)
            cv2.circle(currentImg, (indexFinger[0], indexFinger[1]), 10, (0, 0, 255), cv2.FILLED)
            annotSet = False

    if buttonPressed:
        buttonPressedCount += 1
        if buttonPressedCount > buttonDelay:
            buttonPressed = False
            buttonPressedCount = 0
    # print(annotations[annotInd])
    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(currentImg, annotations[i][j-1], annotations[i][j], (0, 0, 255), 5)
    cv2.imshow("current image", currentImg)
    cv2.imshow("image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
