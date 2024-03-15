import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread(r"C:\Users\tksri\OneDrive\Pictures\85582987f7125e4868fdcb28661e934f.png",cv2.IMREAD_COLOR)
img = cv2.resize(img,(600,600))
cv2.imshow("image",img)
cv2.waitKey(0)
