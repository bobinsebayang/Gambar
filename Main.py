import cv2
from matplotlib import pyplot as plt

print(cv2.__version__)

img = cv2.imread("daun.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(gray, cmap = 'gray')
plt.title("Hasil -gray")

plt.show()