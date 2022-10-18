import cv2
import numpy as np

f1 = int(input("Focal length n°1 (mm) : "))
f2 = int(input("Focal length n°2 (mm) : "))
f3 = int(input("Focal length n°3 (mm) : "))

size_y = int(input("Size (height) in arcsec : "))
size_x = int(input("Size (length) in arcsec : "))

def sample(focal, sizex, sizey):
    winx = 1200  # 6000 / 5
    winy = 800   # 4000 / 5 

    blank = np.zeros((winy, winx, 3), np.uint8)

    sampling = 206*(3.75/focal)
    sizey /= sampling
    sizex /= sampling

    sizey = int(sizey/5)
    sizex = int(sizex/5)

    middlex = int((winx-sizex)/2)
    middley = int((winy-sizey)/2)

    blank[middley:(middley+sizey), middlex:(middlex+sizex)] = (255, 255, 255)
    cv2.imshow("sampler_"+str(f1)+"mm", blank)
    cv2.waitKey(0)

sample(f1, size_x, size_y)
sample(f2, size_x, size_y)
sample(f3, size_x, size_y)
