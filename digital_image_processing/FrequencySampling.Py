import dippykit as dip
import numpy as np
import math
def mse(a1, a2):
	a = a1.size
	b = a2.size
	if a<b:
		a1.resize(a2.shape, refcheck=False)
	else:
		a2.resize(a1.shape, refcheck=False)
	diff = np.subtract(a1, a2)
	sq = np.square(diff)
	mse = sq.mean()
	mse = (100*100)//100
	psnr = 10 * math.log(10, mse)
	print(psnr)
# Read in the lena image and convert it to a normalized float range with im_to_float
im = dip.im_read('airplane.jpg')
im_float = dip.im_to_float(im)

# In case the image isn't grayscale, make it grayscale
if 2 < im_float.ndim:
    im_float = np.mean(im_float, axis=2)

# Use the naming in the problem statement of I1
I0 = im_float
I1 = dip.resample(I0, np.array([[0, .1], [.1, 0]]), interpolation='bilinear')
I2 = dip.resample(I0, np.array([[0, .1], [1, 0]]), interpolation='bilinear')
I3 = dip.resample(I0, np.array([[0, 1], [.1, 0]]), interpolation='bilinear')
I4 = dip.resample(I0, np.array([[2, -1], [-1, 2]]), interpolation='bilinear')
I5 = dip.resample(I0, np.array([[.4, -.2], [-.2, .6]]), interpolation='bilinear')
'''
F1_2 = np.log(np.abs(dip.fftshift(F1)))
F2_2 = np.log(np.abs(dip.fftshift(F2)))
F3_2 = np.log(np.abs(dip.fftshift(F3)))
F4_2 = np.log(np.abs(dip.fftshift(F4)))'''

# Create a figure


'''plot obtained I1, I2, I3, I4'''

dip.figure(1)

dip.subplot(5, 5, 1)
dip.imshow(I0, 'gray')
dip.title('Original Image')

dip.subplot(5, 5, 3)
dip.imshow(I1, 'gray')
dip.title('Filled Image i')

dip.subplot(5, 5, 5)
dip.imshow(I2, 'gray')
dip.title('Image ii')

dip.subplot(5, 5, 7)
dip.imshow(I3, 'gray')
dip.title('Image iii')

dip.subplot(5, 5, 9)
dip.imshow(I4, 'gray')
dip.title('Image iv')

dip.subplot(5, 5, 13)
dip.imshow(I5, 'gray')
dip.title('Image v')
'''
dip.subplot(2, 2, 2)
dip.imshow(I2, 'gray')
dip.title('Horizontally Downsampled in Frequency')

dip.subplot(2, 2, 3)
dip.imshow(I3, 'gray')
dip.title('Vertically Downsampled in Frequency')

dip.subplot(2, 2, 4)
dip.imshow(I4, 'gray')
dip.title('Downsampled in Frequency')'''

# Create a figure



# Show the images
dip.show()

