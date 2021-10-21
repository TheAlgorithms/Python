import numpy as np
import skimage.color
import skimage.filters
import skimage.io
import matplotlib.pyplot as plt

# read and display the original image
image = skimage.io.imread(fname='example.jpg')
# blur and grayscale before thresholding
blur = skimage.color.rgb2gray(image)
blur = skimage.filters.gaussian(blur, sigma=1)
# otsu
hist, bin_edges = np.histogram(blur, bins=256)
bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.
weight1 = np.cumsum(hist)
weight2 = np.cumsum(hist[::-1])[::-1]
weightproduct= weight1[:-1] * weight2[1:]
mean1 = np.cumsum(hist * bin_mids) / weight1
mean2 = (np.cumsum((hist * bin_mids)[::-1]) / weight2[::-1])[::-1]
diffmean=mean1[:-1] - mean2[1:]
inter_class_variance = weightproduct * diffmean ** 2
index_of_max_val = np.argmax(inter_class_variance)
threshold = bin_mids[:-1][index_of_max_val]
# # creating mask
# mask = blur > threshold

# Calculating boundary pixel value and center pixel value
m,n=blur.shape
center_pixel = blur[m//2][n//2]
boundary = np.array([])
boundary = np.append(boundary, np.mean(blur[0, :]))
boundary = np.append(boundary, np.mean(blur[:, 0]))
boundary = np.append(boundary, np.mean(blur[m-1, :]))
boundary = np.append(boundary, np.mean(blur[:, n-1]))
boundary_pixel = np.mean(boundary)


# Using the given assumptions to check for foreground and background
if boundary_pixel <= threshold and center_pixel > threshold:
	mask = blur > threshold
else:
	mask = blur <= threshold

#converting back after selection of foreground and background
sel = np.zeros_like(image)
sel[:,:,2] = 255
sel[mask] = image[mask]

# display the result
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(image)
ax1.set_title("Original")
ax2.imshow(sel)
ax2.set_title("After Otsu")
plt.show()


# references: https://datacarpentry.org/image-processing/07-thresholding/ for reversal to original image(sel part)
