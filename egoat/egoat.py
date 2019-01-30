import numpy as np
import cv2
import time

start_time = time.time()

image = cv2.imread("testimage3.jpg")
#boundaries = [([112,60,86], [187,173,201])]
#G, B, R


hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([20,14,100])
upper = np.array([96,255,255])

# find the colors within the specified boundaries and apply
# the mask
mask = cv2.inRange(hsv, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)

grass = output
bw_image = cv2.cvtColor(grass, cv2.COLOR_HSV2BGR)
bw_image = cv2.cvtColor(bw_image, cv2.COLOR_BGR2GRAY)

new_image = bw_image[:]
threshold = 1
h,b = grass.shape[:2]    

for i in range(h):
    for j in range(b):
        if bw_image[i][j] > threshold:
            new_image[i][j] = 255 #Setting the grass to be White
        else:
            new_image[i][j] = 0 #else setting it to zero.

# show the images
cv2.imshow("b/w", new_image)
cv2.imshow("images", np.hstack([image, output]))

print("%s seconds" % (time.time() - start_time))

cv2.waitKey(0) 