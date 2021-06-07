import torch


class ImageDataLoader:

    # ImageDataLoader

    def __init__(self, reader, batch_size: int, shuffle: bool = True):

        self.dataset = reader.dataset
        self.batch_size = batch_size
        self.shuffle = shuffle

        self.DataLoader = torch.utils.data.DataLoader(
            dataset=self.dataset, batch_size=self.batch_size, shuffle=self.shuffle
        )
        self.num_batches = (
            len(self.DataLoader.dataset) + self.DataLoader.batch_size
        ) // self.DataLoader.batch_size

    def next_iter(self):
        return next(iter(self.DataLoader))

    def load(self):
        for i in range(self.num_batches):
            yield next(iter(self.DataLoader))

    def __len__(self):
        return len(self.DataLoader.dataset)

    # def __iter__():
