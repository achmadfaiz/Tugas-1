import numpy as np
import cv2

gambar = cv2.imread('D:\kazanan.jpg',0)
cv2.imwrite('kazanan_grayscale.jpg',gambar)
