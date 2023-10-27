# import the necessary packages
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from scipy import ndimage
import numpy as np
import imutils
import cv2


def watershed_image(path_image: str) -> None:
    """
    Watershed is a classic algorithm used for segmentation, specially when
    has overlapping objects in images.
    """
    # Load the image and perform pyramid mean shift filtering
    image = cv2.imread("/content/watershed_coins_01.webp")
    shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)

    # Convert image to grayscale, then apply Otsu's thresholding
    gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Compute Euclidean distance, then find peaks in this distance map
    D = ndimage.distance_transform_edt(thresh)
    local_max = peak_local_max(D, indices=False, min_distance=20, labels=thresh)
    # Apply the Watershed algorithm
    markers = ndimage.label(local_max, structure=np.ones((3, 3)))[0]
    labels = watershed(-D, markers, mask=thresh)

    # Loop over the unique labels returned by the Watershed algorithm
    for label in np.unique(labels):
        # Ignore label zero (background)
        if label == 0:
            continue
        # Otherwise, draw mask
        mask = np.zeros(gray.shape, dtype="uint8")
        mask[labels == label] = 255
        # Detect contours in the mask and grab the largest one
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key=cv2.contourArea)
        # Draw a circle enclosing the object
        ((x, y), r) = cv2.minEnclosingCircle(c)
        cv2.circle(image, (int(x), int(y)), int(r), (0, 255, 0), 2)
        cv2.putText(
            image,
            f"#{label}",
            (int(x) - 10, int(y)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2,
        )
    # Dhow the output image
    cv2.imshow("Result image", image)


if __name__ == "__main__":
    watershed_image("PATH_TO_YOUR_IMAGE")
    waitKey(0)
    destroyAllWindows()
