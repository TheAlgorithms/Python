"""
VGG16 Model Implementation

Paper: https://arxiv.org/abs/1409.1556
"""

import torch
from torch import nn


class VGG16(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()

        # -------------------------- Feature Extraction Layers --------------------- #
        # The feature extraction layers consist of a series of convolutional and
        # max-pooling layers that learn hierarchical representations of input images.
        # The architecture follows a pattern of multiple convolutional layers with
        # ReLU activations, followed by max-pooling layers.
        # The number of convolutional layers per block increases as the network
        # goes deeper, and the number of output channels doubles after each
        # max-pooling layer.
        # -------------------------------------------------------------------------- #

        self.features = nn.Sequential(
            # Layer 1
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            # Layer 2
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # Layer 3
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            # Layer 4
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # Layer 5
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            # Layer 6
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            # Layer 7
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # Layer 8
            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            # Layer 9
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            # Layer 10
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            # Layer 11
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            # Layer 12
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            # Layer 13
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        self.avgpool = nn.AdaptiveAvgPool2d((7, 7))

        # -------------------------- Fully Connected Layers -------------------------- #
        # These layers receive the high-level features learned by the feature extraction
        # layers and use them to perform the final classification task.
        # The fully connected layers consist of three linear layers with ReLU
        # activations and dropout for regularization. The final layer has a
        # number of output units equal to the number of classes in the
        # classification problem.
        # ---------------------------------------------------------------------------- #

        self.classifier = nn.Sequential(
            # Layer 14
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            # Layer 15
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            # Layer 16
            nn.Linear(4096, num_classes),
        )

    def forward(self, image):
        image = self.features(image)
        image = self.avgpool(image)
        image = torch.flatten(image, 1)
        image = self.classifier(image)
        return image


def test_model(image_tensor: torch.tensor) -> bool:
    """
    Test the model for a batch of 64 images

    Args:
        image_tensor (torch.tensor): Batch of 64 Images for the model.

    Returns:
        bool: True if the model works, False otherwise

    >>> test_model(torch.rand(64, 3, 224, 224))
    True
    """

    try:
        model = VGG16()
        output = model(image_tensor)

    except Exception as e:
        print(e)
        return False

    return output.shape == torch.Size([64, 10])


if __name__ == "__main__":
    random_image_1 = torch.randn(64, 3, 224, 224)
    random_image_2 = torch.randn(3, 224, 224)

    print(f"random_image_1 Model Passed: {test_model(random_image_1)}")
    print(f"\nrandom_image_2 Model Passed: {test_model(random_image_2)}")
