"""
Segmentation Algorithm

Example of segmentation of images consisting of one object to be differentiated from a
simple background. Running the script in its state retrieves a image of a brazilian coin
and crops the original image to better focus on the coin.

The image used as example is from a Kaggle competition for coin classification.
Link for the original competition and database:
    https://www.kaggle.com/lgmoneda/br-coins

The SciKit-Image library is used to perform the image retrieving and operations:
    https://scikit-image.org/

Although the example shows a coin, the algorithm crops the first thing in a given image
that forms a closed region.
"""

# Modules used for image filtering
from skimage import filters
from skimage.color import rgb2hsv

# Modules used for segmentation
from skimage import util
from skimage.morphology import label
from skimage.measure import regionprops

# Other modules
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.transform import resize


def binarizeImage(img):
    """
    Function used to filter and apply threshold on a given image
    """

    # Load image in HSV channels
    hsv = rgb2hsv(img)

    # Retrive only the brightness channel
    channel_s = hsv[:, :, 1]

    # Filter the brightness channel with a local median
    # comparing the image matrix with a 3x3 ones matrix
    channel_filtered = filters.median(channel_s, np.ones((3, 3)))

    # Define a threshold for filtering the image based on the Otsu's method
    # More about Otsu's method: https://en.wikipedia.org/wiki/Otsu%27s_method
    block_size = 20
    local_thresh = filters.threshold_otsu(channel_filtered, block_size)

    # Define the binary image as a matrix resulting from the comparisson
    # of the filtered image and the calculated threshold
    binary_s = channel_filtered > local_thresh

    return binary_s


def cropCoinFromBinary(img, binarizedImg):
    """
    Function used to crop a closed region from an image based on its binarized form

    The retrieved image is only considered valid if it has minimum area of 20 pixels
    and its proportions do not deviate much from a square
    """

    # Read the image in a more useful format
    binary = util.img_as_ubyte(binarizedImg)

    # Recognize connected borders in the image
    labeled = label(binary)

    # Measure properties of labeled image regions
    regions = regionprops(labeled)

    for region in regions:
        # Skip imagens with less than 20 pixels of area
        if region["Area"] < 20:
            continue

        # Retrieve bounding box coordinates
        min_h, min_w, max_h, max_w = region["BoundingBox"]

        # Calculate region ratio
        ratio = (max_w - min_w) / (max_h - min_h)

        # Skip regions with not square proportions
        if not (0.90 < ratio < 1.10):
            continue

        # Set offset for proper crop of coin
        offset = 5

        # Crop from original image based on region
        cropedImg = img[
            min_h - offset : max_h + offset, min_w - offset : max_w + offset
        ]

        return cropedImg


if __name__ == "__main__":
    imgs = []
    cropeds = []
    not_cropeds = []

    # Example image from original Kaggle competition for brazilian coin classification
    # Link for Kaggle competition: https://www.kaggle.com/lgmoneda/br-coins
    example_url = (
        "https://storage.googleapis.com/kagglesdsdata/datasets/1129/1135640/"
        "COCO_labelme_classification/classification/100_1477154436.jpg?X-Goog-Algorithm"
        "=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.g"
        "serviceaccount.com%2F20211022%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=202"
        "11022T173018Z&X-Goog-Expires=345599&X-Goog-SignedHeaders=host&X-Goog-Signature"
        "=5caa237b69a5f61636d21343f16c679b43920808ba4521868e813bf8652bf10df765d181c4dcf"
        "e595e5779149d73e7b6ada9398b1ebe73c4b012064c38a4445fed1445084da751f8c89f81064eb"
        "4b951b2b6110bced4502b599ca333d903e1bf7fde9e5e6869e39264eb2e6802123e4806748beb8"
        "ec7ddb0fcec58cab2dc6a287dcd5640bdd08cedbc3526ea60adf34a1186836fe2dd4f8d553d304"
        "09f76c002db3ce33a32dd528f5066739724ee862a37b1a90e0d37d985bc2fc9b0259a6cc7b64af"
        "a19d22332455745d29e62742f3e7b128f1e99766f1969764708046a24d4a14cc95f61380c1aaf9"
        "c8768a44a9ed1bd80fc782182bb6306fa12efe8008688"
    )

    # Retrive image from url. Skimage imread is capable of retrieving images from urls
    imgs.append(io.imread(example_url))

    # Iterate our images, we use enumerate for extra info
    for cont, img in enumerate(imgs):

        try:
            # Binarize the image
            bin = binarizeImage(img)

            # Crop the image based on the binary of the same image
            croped_img = cropCoinFromBinary(img, bin)

            # Verifies if the returned image is None, in which case the function was
            # not able to recognize a region
            if isinstance(img, type(None)):
                print("NoneType crop ", cont)
                continue

            # Verifies if the image has width or height equals 0, making it invalid
            if croped_img.shape[1] == 0 or croped_img.shape[0] == 0:
                not_cropeds.append(img)
                print("0 sized image ", cont)
                continue

            cropeds.append(croped_img)
        except TypeError:
            not_cropeds.append(img)
            print("Error on img ", cont)
            continue

    # Plot normalized image
    plt.imshow(
        resize(
            cropeds[0] if len(cropeds) > 0 else not_cropeds[0],
            (128, 128),
            anti_aliasing=True,
        )
    )
    plt.show()
