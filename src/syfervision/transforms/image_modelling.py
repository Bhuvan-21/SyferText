import torch
from torchvision import transforms


class ToTensor:
    def __init__(self):
        self.transform = transforms.ToTensor()

    def __call__(self, x):
        return self.transform(x)


class Resize:
    def __init__(self, size):
        self.transform = transforms.Resize(size)

    def __call__(self, x):
        return self.transform(x)
