import numpy as np
import cv2
import warnings
warnings.filterwarnings("ignore")

img = cv2.imread('PE09_input.jpeg', 1)
row,col,ch = img.shape
p = 0.5
a = 0.009
noisy = img

  # Salt mode
num_salt = np.ceil(a * img.size * p)
coords = [np.random.randint(0, i - 1, int(num_salt))
          for i in img.shape]
noisy[coords] = 1

  # Pepper mode
num_pepper = np.ceil(a * img.size * (1. - p))
coords = [np.random.randint(0, i - 1, int(num_pepper))
          for i in img.shape]
noisy[coords] = 0

cv2.imshow('Input image with black and white noise', noisy)

median_blur= cv2.medianBlur(noisy, 5)
cv2.imshow('Output image after median filter', median_blur)  

cv2.waitKey()
cv2.destroyAllWindows()