class InfiniteList:
    def __init__(self, *args, fill_value=None):
        self.items = list(args)
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __setitem__(self, index: int, item) -> None:
        for i in range(index - len(self.items)):
            self.items[i] = None
        self.items[index] = item

    def __str__(self):
        return ','.join(self.items)
