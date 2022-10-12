import cv2
import matplotlib.pyplot as plt
import numpy as np

cell = np.array(
    [
        [0, 1, 2, 5, 5, 5, 5, 5],
        [0, 0, 1, 4, 4, 5, 5, 5],
        [0, 0, 1, 3, 4, 5, 5, 5],
        [0, 0, 0, 1, 2, 3, 5, 5],
        [0, 0, 0, 0, 1, 2, 5, 5],
        [0, 0, 0, 0, 0, 1, 3, 5],
        [0, 0, 0, 0, 0, 0, 2, 5],
        [0, 0, 0, 0, 0, 0, 1, 3],
    ],
    dtype="float64",
)

# compute the gradients in the x and y directions:
gradx = cv2.Sobel(cell, cv2.CV_64F, 1, 0, ksize=1)
grady = cv2.Sobel(cell, cv2.CV_64F, 0, 1, ksize=1)
# compute the magnitude and angle of the gradients
norm, angle = cv2.cartToPolar(gradx, grady, angleInDegrees=True)

plt.figure(figsize=(10, 5))

# display the image
plt.subplot(1, 2, 1)
plt.imshow(cell, cmap="binary", origin="lower")

# display the magnitude of the gradients:
plt.subplot(1, 2, 2)
plt.imshow(norm, cmap="binary", origin="lower")
# and superimpose an arrow showing the gradient
# magnitude and direction:
q = plt.quiver(gradx, grady, color="blue")
plt.savefig("gradient.png")
plt.show()
