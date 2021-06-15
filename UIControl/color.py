import cv2
import numpy as np

def color_detect(top_color, pant_color, pant,path):
    result, ratio, result2, ratio2 = 0, 0, 0, 0
    basic_color = {"RED": 0, "ORANGE": 15, "YELLOW": 30, "CHARTREUSE_GREEN": 45,
                   "GREEN": 60, "SPRING_GREEN": 75, "CYAN": 90, "AZURE": 105,
                   "BLUE": 120, "VIOLET": 135, "MAGENTA": 150, "ROSE": 165,
                   "BLACK": 256, "WHITE": 50, "GRAY": 16}
    img = cv2.imread("runs/detect/exp/crops/person/" + str(path))
    height, width, channel = img.shape

    img_1 = img[0: round(3 * height / 5), :]
    img_2 = img[round(2 * height / 5): height, :]

    img_1_hsv = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV)
    h1, s1, v1 = cv2.split(img_1_hsv)
    img_2_hsv = cv2.cvtColor(img_2, cv2.COLOR_BGR2HSV)
    h2, s2, v2 = cv2.split(img_2_hsv)

    # 추출 색깔 초기화
    color_1 = basic_color[top_color]
    color_2 = basic_color[pant_color]

    standard_ratio = 0.15

    # BLACK
    if color_1 == 256:
        lower = (0, 0, 0)
        upper = (179, 128, 30)

        img_mask = cv2.inRange(img_1_hsv, lower, upper)
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # WHITE
    elif color_1 == 50:
        lower = (0, 0, 175)
        upper = (179, 25, 255)

        img_mask = cv2.inRange(img_1_hsv, lower, upper)
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # GRAZY
    elif color_1 == 16:
        lower = (0, 0, 75)
        upper = (179, 25, 175)

        img_mask = cv2.inRange(img_1_hsv, lower, upper)
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # RED
    elif color_1 == 0:
        img_mask = cv2.inRange(img_1_hsv, (0, 128, 128), (10, 255, 255))
        img_mask2 = cv2.inRange(img_1_hsv, (170, 128, 128), (180, 255, 255))
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask) + np.count_nonzero(
            img_mask2 == 255) / np.size(img_mask2)
    # ETC
    else:
        img_mask = cv2.inRange(h1, color_1 - 10, color_1 + 10)
        ratio = np.count_nonzero(img_mask == 255) / np.size(img_mask)

    if ratio >= standard_ratio:
        result += 40

    if pant == "shorts":
        standard_ratio = 0.1

    # BLACK
    if color_2 == 256:
        lower = (0, 0, 0)
        upper = (179, 255, 30)
        img_mask = cv2.inRange(img_2_hsv, lower, upper)
        ratio2 = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # WHITE
    elif color_2 == 50:
        lower = (0, 0, 175)
        upper = (179, 25, 255)

        img_mask = cv2.inRange(img_2_hsv, lower, upper)
        ratio2 = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # GRAZY
    elif color_2 == 16:
        lower = (0, 0, 75)
        upper = (179, 25, 175)

        img_mask = cv2.inRange(img_2_hsv, lower, upper)
        ratio2 = np.count_nonzero(img_mask == 255) / np.size(img_mask)
    # RED
    elif color_2 == 0:
        img_mask = cv2.inRange(img_2_hsv, (0, 128, 128), (10, 255, 255))
        img_mask2 = cv2.inRange(img_2_hsv, (170, 128, 128), (180, 255, 255))
        ratio2 = np.count_nonzero(img_mask == 255) / np.size(img_mask) + np.count_nonzero(
            img_mask2 == 255) / np.size(
            img_mask2)
    # ETC
    else:
        img_mask = cv2.inRange(h2, color_2 - 10, color_2 + 10)
        ratio2 = np.count_nonzero(img_mask == 255) / np.size(img_mask)

    if ratio2 >= standard_ratio:
        result2 += 40

    return result, result2, ratio, ratio2