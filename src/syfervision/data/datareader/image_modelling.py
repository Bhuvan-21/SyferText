import torch
from torchvision import datasets, transforms
from .. import datameta


class ImageDataReader:

    # ImageDataReader

    def __init__(self, meta: datameta.ImageDataMeta, mode: str, transforms_):

        self.path = ""
        if mode == "train":
            self.path = meta.train_path
        elif mode == "valid":
            self.path = meta.valid_path
        elif mode == "test":
            self.path = meta.test_path

        self.transforms_ = transforms_

        self.dataset = datasets.ImageFolder(
            self.path, transform=transforms.Compose(self.transforms_)
        )
