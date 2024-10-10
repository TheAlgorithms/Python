"""
Generative Adversarial Network

Objective : To train a GAN model to generate handwritten digits that can be transferred to other domains.

Resources GAN Theory :
    https://en.wikipedia.org/wiki/Generative_adversarial_network
Resources PyTorch: https://pytorch.org/

Download dataset from :
PyTorch internal function

1. Fetch the Dataset with PyTorch function.
2. Create Dataloader.
3. Create Discriminator and Generator.
4. Set the hyperparameters and models.
5. Set the loss functions.
6. Create the training loop.
7. Visualize the losses.
8. Visualize the result from GAN.

"""

import numpy as np
import torch
import matplotlib.pyplot as plt
from torchvision import datasets
import torchvision.transforms as transforms

# number of subprocesses to use for data loading
num_workers = 0
# how many samples per batch to load
batch_size = 64

# convert data to torch.FloatTensor
transform = transforms.ToTensor()

# get the training datasets
train_data = datasets.MNIST(root="data", train=True, download=True, transform=transform)

# prepare data loader
train_loader = torch.utils.data.DataLoader(
    train_data, batch_size=batch_size, num_workers=num_workers
)

import torch.nn as nn
import torch.nn.functional as F

# Creating Generator and Discriminator for GAN


class discriminator(nn.Module):
    def __init__(self, input_size, output_size, hidden_dim):
        super(discriminator, self).__init__()

        # defining the layers of the discriminator
        self.fc1 = nn.Linear(input_size, hidden_dim * 4)
        self.fc2 = nn.Linear(hidden_dim * 4, hidden_dim * 2)
        self.fc3 = nn.Linear(hidden_dim * 2, hidden_dim)
        # final fully connected layer
        self.fc4 = nn.Linear(hidden_dim, output_size)
        # dropout layer
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        # pass x through all layers
        # apply leaky relu activation to all hidden layers
        x = x.view(-1, 28 * 28)  # flattening the image
        x = F.leaky_relu(self.fc1(x), 0.2)
        x = self.dropout(x)
        x = F.leaky_relu(self.fc2(x), 0.2)
        x = self.dropout(x)
        x = F.leaky_relu(self.fc3(x), 0.2)
        x = self.dropout(x)
        x_out = self.fc4(x)

        return x_out


class generator(nn.Module):
    def __init__(self, input_size, output_size, hidden_dim):
        super(generator, self).__init__()

        # define all layers
        self.fc1 = nn.Linear(input_size, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim * 2)
        self.fc3 = nn.Linear(hidden_dim * 2, hidden_dim * 4)
        # final layer
        self.fc4 = nn.Linear(hidden_dim * 4, output_size)
        # dropout layer
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        # pass x through all layers
        # final layer should have tanh applied
        x = F.leaky_relu(self.fc1(x), 0.2)
        x = self.dropout(x)
        x = F.leaky_relu(self.fc2(x), 0.2)
        x = self.dropout(x)
        x = F.leaky_relu(self.fc3(x), 0.2)
        x = self.dropout(x)
        x_out = F.tanh(self.fc4(x))
        return x_out


# Calculate losses
def real_loss(D_out, smooth=False):
    # compare logits to real labels
    # smooth labels if smooth=True
    # puting it into cuda
    batch_size = D_out.size(0)
    if smooth:
        labels = torch.ones(batch_size).cuda() * 0.9
    else:
        labels = torch.ones(batch_size).cuda()
    criterion = nn.BCEWithLogitsLoss()
    loss = criterion(D_out.squeeze(), labels)
    return loss


def fake_loss(D_out):
    # compare logits to fake labels
    batch_size = D_out.size(0)
    labels = torch.zeros(batch_size).cuda()
    criterion = nn.BCEWithLogitsLoss()
    loss = criterion(D_out.squeeze(), labels)
    return loss


# Discriminator hyperparams
# Size of input image to discriminator (28*28)
input_size = 784
# Size of discriminator output (real or fake)
d_output_size = 1
# Size of *last* hidden layer in the discriminator
d_hidden_size = 32

# Generator hyperparams

# Size of latent vector to give to generator
z_size = 100
# Size of discriminator output (generated image)
g_output_size = 784
# Size of *first* hidden layer in the generator
g_hidden_size = 32

# instantiate discriminator and generator and put it in cuda mode
D = discriminator(input_size, d_output_size, d_hidden_size).cuda()
G = generator(z_size, g_output_size, g_hidden_size).cuda()

import pickle as pkl

# training hyperparams
num_epochs = 40

# keep track of loss and generated, "fake" samples
samples = []
losses = []

print_every = 400

# Get some fixed data for sampling. These are images that are held
# constant throughout training, and allow us to inspect the model's performance
sample_size = 16
fixed_z = np.random.uniform(-1, 1, size=(sample_size, z_size))
fixed_z = torch.from_numpy(fixed_z).float().cuda()

# train the network
D.train()
G.train()
for epoch in range(num_epochs):
    for batch_i, (real_images, _) in enumerate(train_loader):
        batch_size = real_images.size(0)

        ## Important rescaling step ##
        real_images = (
            real_images * 2 - 1
        ).cuda()  # rescale input images from [0,1) to [-1, 1)

        # ============================================
        #            TRAIN THE DISCRIMINATOR
        # ============================================
        d_optimizer.zero_grad()
        # 1. Train with real images

        # Compute the discriminator losses on real images
        # use smoothed labels
        D_real = D(real_images)
        d_real_loss = real_loss(D_real, smooth=True)
        # 2. Train with fake images

        # Generate fake images
        z = np.random.uniform(-1, 1, size=(batch_size, z_size))
        z = torch.from_numpy(z).float().cuda()
        fake_images = G(z)

        # Compute the discriminator losses on fake images
        D_fake = D(fake_images)
        d_fake_loss = fake_loss(D_fake)
        # add up real and fake losses and perform backprop
        d_loss = d_real_loss + d_fake_loss
        d_loss.backward()
        d_optimizer.step()

        # =========================================
        #            TRAIN THE GENERATOR
        # =========================================
        g_optimizer.zero_grad()
        # 1. Train with fake images and flipped labels

        # Generate fake images
        z = np.random.uniform(-1, 1, size=(batch_size, z_size))
        z = torch.from_numpy(z).float().cuda()
        fake_images = G(z)
        # Compute the discriminator losses on fake images
        # using flipped labels!
        D_fake = D(fake_images)
        # perform backprop
        g_loss = real_loss(D_fake)
        g_loss.backward()
        g_optimizer.step()

        # Print some loss stats
        if batch_i % print_every == 0:
            # print discriminator and generator loss
            print(
                "Epoch [{:5d}/{:5d}] | d_loss: {:6.4f} | g_loss: {:6.4f}".format(
                    epoch + 1, num_epochs, d_loss.item(), g_loss.item()
                )
            )

    ## AFTER EACH EPOCH##
    # append discriminator loss and generator loss
    losses.append((d_loss.item(), g_loss.item()))

    # generate and save sample, fake images
    G.eval()  # eval mode for generating samples
    samples_z = G(fixed_z)
    samples.append(samples_z)
    G.train()  # back to train mode


# Save training generator samples
with open("train_samples.pkl", "wb") as f:
    pkl.dump(samples, f)

# ploting Discriminator and Generator loss
fig, ax = plt.subplots()
losses = np.array(losses)
plt.plot(losses.T[0], label="Discriminator")
plt.plot(losses.T[1], label="Generator")
plt.title("Training Losses")
plt.legend()
plt.show()


# Viewing the results of the GAN
def view_samples(epoch, samples):
    fig, axes = plt.subplots(figsize=(7, 7), nrows=4, ncols=4, sharey=True, sharex=True)
    fig.suptitle("Generated Digits")
    for ax, img in zip(axes.flatten(), samples[epoch]):
        img = img.detach().cpu().numpy()
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        im = ax.imshow(img.reshape((28, 28)), cmap="Greys_r")


with open("train_samples.pkl", "rb") as f:
    samples = pkl.load(f)

view_samples(-1, samples)
plt.show()
