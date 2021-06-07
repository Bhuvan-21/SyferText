class ImageDataMeta:

    # Image Meta Data

    def __init__(self, train_path: str, valid_path: str = None, test_path: str = None):

        self.train_path = train_path
        self.valid_path = valid_path
        self.test_path = test_path
