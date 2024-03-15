import cv2
path = r"C:\Users\tksri\OneDrive\Pictures\85582987f7125e4868fdcb28661e934f.png"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow(window_name, image)
cv2.waitKey(0)
