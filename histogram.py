import cv2
import numpy as np

gambar = cv2.imread('D:\kazanan.jpg',0)

equ = cv2.equalizeHist(gambar)
res = np.hstack((gambar,equ)) #stacking images side-by-side

cv2.imwrite('kazanan_histogram.jpg',res)
