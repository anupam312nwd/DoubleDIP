#!/usr/bin/env python3
""" Intro and loading images"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

cartoon = cv2.imread('data/cartoon.jpg')
bean = cv2.imread('data/bean.jpg')

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

# cv2.imwrite('data/build.png', img)
# cv2.imshow('building', building)
# cv2.imshow('peas', peas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# mix1 = cv2.addWeighted(bean, 0.1, cartoon, 0.9, 0)
# mix2 = cv2.addWeighted(bean, 0.2, cartoon, 0.8, 0)
# mix3 = cv2.addWeighted(bean, 0.3, cartoon, 0.7, 0)
# mix4 = cv2.addWeighted(bean, 0.4, cartoon, 0.6, 0)
# mix5 = cv2.addWeighted(bean, 0.5, cartoon, 0.5, 0)
# mix6 = cv2.addWeighted(bean, 0.6, cartoon, 0.4, 0)
# mix7 = cv2.addWeighted(bean, 0.7, cartoon, 0.3, 0)
# mix8 = cv2.addWeighted(bean, 0.8, cartoon, 0.1, 0)
# mix9 = cv2.addWeighted(bean, 0.9, cartoon, 0.1, 0)


# cv2.imshow('mix', mix)
# cv2.imshow('mix_weighted', mix_weighted)
# cv2.imshow('peas', peas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

for i in range(1, 10):
    globals()['mix'+str(i)] = cv2.addWeighted(bean, i/10.0, cartoon, 1-i/10.0, 0)
    img = globals()['mix'+str(i)]
    cv2.imwrite('data/mix'+str(i)+'.png', img)
# print(building)
