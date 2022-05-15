import cv2
import numpy as np

def grid(path):
    path = "maze3.jpg"
    img = np.array(cv2.imread(path))
    img = cv2.resize(img, (25,25))

    # cv2.imshow("--", img)
    (rows, cols, channels) = img.shape
    # print((rows, cols, channels))
    mat = np.full_like(img, (255, 255, 255))

    black_mask = cv2.inRange(img, (0,0,0), (50,50,50))
    white_mask = cv2.inRange(img, (200,200,200), (255,255,255))
    red_mask = cv2.inRange(img, (0,0,220), (50,50,255))
    green_mask = cv2.inRange(img, (0,220,0), (50,255,50))
    mat[black_mask != 0] = [0,0,0]
    mat[white_mask != 0] = [255,255,255]
    mat[red_mask != 0] = [0,0,255]
    mat[green_mask != 0] = [255,0,0]

    final = np.full((rows,cols)," ",dtype=object)
    final[black_mask != 0] = "+"
    final[white_mask != 0] = " "
    final[red_mask != 0] = "s"
    final[green_mask != 0] = "e"
    # print(final.shape)

    # cv2.imshow("__", mat)

    # print(final)
    return(final)
