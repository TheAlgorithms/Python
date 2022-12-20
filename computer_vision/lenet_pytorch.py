"""
LeNet Network

Paper: http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf
"""

import numpy
import torch
import torch.nn as nn


class LeNet(nn.Module):
    def __init__(self) -> None:
        super().__init__()

        self.tanh = nn.Tanh()
        self.avgpool = nn.AvgPool2d(kernel_size=2, stride=2)

        self.conv1 = nn.Conv2d(
            in_channels=1,
            out_channels=6,
            kernel_size=(5, 5),
            stride=(1, 1),
            padding=(0, 0),
        )
        self.conv2 = nn.Conv2d(
            in_channels=6,
            out_channels=16,
            kernel_size=(5, 5),
            stride=(1, 1),
            padding=(0, 0),
        )
        self.conv3 = nn.Conv2d(
            in_channels=16,
            out_channels=120,
            kernel_size=(5, 5),
            stride=(1, 1),
            padding=(0, 0),
        )

        self.linear1 = nn.Linear(120, 84)
        self.linear2 = nn.Linear(84, 10)

    def forward(self, image_array: numpy.ndarray) -> numpy.ndarray:
        image_array = self.tanh(self.conv1(image_array))
        image_array = self.avgpool(image_array)
        image_array = self.tanh(self.conv2(image_array))
        image_array = self.avgpool(image_array)
        image_array = self.tanh(self.conv3(image_array))

        image_array = image_array.reshape(image_array.shape[0], -1)
        image_array = self.tanh(self.linear1(image_array))
        image_array = self.linear2(image_array)
        return image_array


def test_model(image_tensor: torch.tensor) -> bool:
    """
    Test the model on an input batch of 64 images

    Args:
        image_tensor (torch.tensor): Batch of Images for the model

    >>> test_model(torch.randn(64, 1, 32, 32))
    True

    """
    try:
        model = LeNet()
        output = model(image_tensor)
    except RuntimeError:
        return False

    return output.shape == torch.zeros([64, 10]).shape


if __name__ == "__main__":
    random_image_1 = torch.randn(64, 1, 32, 32)
    random_image_2 = torch.randn(1, 32, 32)

    print(f"random_image_1 Model Passed: {test_model(random_image_1)}")
    print(f"\nrandom_image_2 Model Passed: {test_model(random_image_2)}")
