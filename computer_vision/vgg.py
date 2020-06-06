import torch
import torch.nn as nn


class VGG(nn.Module):
    def __init__(self, cfg: list):
        super(VGG, self).__init__()
        self.net = self.build(cfg)

    def build(self, cfg):
        # Build the network based on the config
        layers = []
        n_channels = 1
        for i in cfg:
            if i == "2P":
                layers.append(nn.MaxPool2d(kernel_size=2, stride=2))
            else:
                layers.append(nn.Conv2d(n_channels, i, kernel_size=3, padding=1))
                layers.append(nn.ReLU())
                n_channels = i
                # layers.append(nn.Conv2d(n_channels, i, kernel_size = 3, padding=1),nn.ReLU())
        # layers.append(nn.Linear(4096,4096))
        # layers.append(nn.ReLU())
        # layers.append(nn.Linear(4096,4096))
        # layers.append(nn.ReLU())
        # layers.append(nn.Linear(4096,10))
        # layers.append(nn.Softmax())
        # print(layers)
        return nn.Sequential(*layers)

    def forward(self, x):
        # Do the forward pass, return the output
        x = x.view(-1, 1, 28, 28)
        return self.net(x)

    def __str__(self):
        return f"VGG for feature extraction : \n {self.net}"


# cfg = {
#     'A': [64, '2P', 128, '2P',  256, 256, '2P']}

cfg = {
    "A": [64, "2P", 128, "2P", 256, 256, "2P", 512, 512, "2P", 512, 512, "2P"],
    "B": [64, 64, "2P", 128, 128, "2P", 256, 256, "2P", 512, 512, "2P", 512, 512, "2P"],
    "D": [
        64,
        64,
        "2P",
        128,
        128,
        "2P",
        256,
        256,
        256,
        "2P",
        512,
        512,
        512,
        "2P",
        512,
        512,
        512,
        "2P",
    ],
    "E": [
        64,
        64,
        "2P",
        128,
        128,
        "2P",
        256,
        256,
        256,
        256,
        "2P",
        512,
        512,
        512,
        512,
        "2P",
        512,
        512,
        512,
        512,
        "2P",
    ],
}

network = VGG(cfg["B"])
print(network)
# exit()
inp = torch.randn([28, 28])
print(inp)
a = network(inp)
print(a.shape)
