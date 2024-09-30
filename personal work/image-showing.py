# Arden Boettcher
# 9/25/24
# Image showing

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('image.png')

# Display the image
imgplot = plt.imshow(img)
plt.show()