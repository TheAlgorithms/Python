import cv2
import numpy as np


class MeanShiftSegmentation:
    def __init__(self, spatial_radius, color_radius, min_density):
        self.spatial_radius = spatial_radius
        self.color_radius = color_radius
        self.min_density = min_density

    def mean_shift(self, data):
        shifted_data = data.copy()
        for i in range(len(data)):
            x, y, color = data[i]
            x_new, y_new, color_new = x, y, color
            weight_total = 0.0
            for j in range(len(data)):
                x_j, y_j, color_j = data[j]
                spatial_dist = np.sqrt((x - x_j) ** 2 + (y - y_j) ** 2)
                color_dist = np.linalg.norm(color - color_j)
                spatial_weight = np.exp(
                    -0.5 * (spatial_dist / self.spatial_radius) ** 2
                )
                color_weight = np.exp(-0.5 * (color_dist / self.color_radius) ** 2)
                weight = spatial_weight * color_weight
                x_new += x_j * weight
                y_new += y_j * weight
                color_new += color_j * weight
                weight_total += weight
            x_new /= weight_total
            y_new /= weight_total
            color_new /= weight_total
            shifted_data[i] = [x_new, y_new, color_new]
        return shifted_data

    def segment(self, image_path):
        image = cv2.imread(image_path)
        height, width, _ = image.shape
        data = [(x, y, color) for (y, x), color in np.ndenumerate(image)]
        data = self.mean_shift(data)

        labels = np.zeros((height, width), dtype=int)
        label_count = 0
        label_dict = {}

        for y in range(height):
            for x in range(width):
                if labels[y, x] == 0:
                    label_count += 1
                    labels[y, x] = label_count
                    label_dict[label_count] = [data[y * width + x]]

                for j in range(y - 1, y + 2):
                    for i in range(x - 1, x + 2):
                        if j < 0 or j >= height or i < 0 or i >= width:
                            continue
                        if labels[j, i] != 0:
                            if (
                                np.linalg.norm(
                                    data[y * width + x][:2] - data[j * width + i][:2]
                                )
                                < self.color_radius
                            ):
                                labels[y, x] = labels[j, i]
                                break

                if labels[y, x] not in label_dict:
                    label_dict[labels[y, x]] = [data[y * width + x]]
                else:
                    label_dict[labels[y, x]].append(data[y * width + x])

        for label in label_dict:
            if len(label_dict[label]) < self.min_density:
                for data_point in label_dict[label]:
                    y, x, _ = data_point
                    labels[y, x] = 0

        return labels


if __name__ == "__main__":
    segmentation = MeanShiftSegmentation(
        spatial_radius=10, color_radius=30, min_density=50
    )
    labels = segmentation.segment("path_to_image.jpg")

    # Create a color map for visualization
    colormap = np.random.randint(0, 255, size=(np.max(labels) + 1, 3))
    colored_labels = colormap[labels]

    cv2.imshow("Mean-Shift Segmentation", colored_labels)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
