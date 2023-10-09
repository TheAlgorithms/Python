import cv2
import numpy as np


class HarrisCorner:
    def __init__(self, k: float, window_size: int):
        if k not in (0.04, 0.06):
            raise ValueError("Invalid k value")
        self.k = k
        self.window_size = window_size

    def detect(self, img: np.ndarray) -> np.ndarray:
        dy, dx = np.gradient(img)
        ixx = dx**2
        iyy = dy**2
        ixy = dx * dy

        offset = self.window_size // 2
        h, w = img.shape

        corner_list = []

        for y in range(offset, h - offset):
            for x in range(offset, w - offset):
                wxx = ixx[
                    y - offset : y + offset + 1, x - offset : x + offset + 1
                ].sum()
                wyy = iyy[
                    y - offset : y + offset + 1, x - offset : x + offset + 1
                ].sum()
                wxy = ixy[
                    y - offset : y + offset + 1, x - offset : x + offset + 1
                ].sum()

                det = (wxx * wyy) - (wxy**2)
                trace = wxx + wyy
                r = det - self.k * (trace**2)

                if r > 0.5:
                    corner_list.append([x, y, r])

        return np.array(corner_list)


if __name__ == "__main__":
    try:
        img = cv2.imread("path_to_image", 0)
        edge_detector = HarrisCorner(0.04, 3)
        corners = edge_detector.detect(img)

        color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        for corner in corners:
            x, y, _ = map(int, corner)
            color_img[y, x] = [0, 0, 255]

        cv2.imwrite("detect.png", color_img)

    except Exception as e:
        print(f"Error: {e}")
