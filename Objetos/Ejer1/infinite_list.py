class InfiniteList:
    def __init__(self, *args, fill_value=None):
        self.args = list(args)
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        return self.args[index]

    def __len__(self):
        return len(self.args)

    def __setitem__(self, index: int, item) -> None:
        if index >= len(self.args):
            self.args.extend([self.fill_value] * (index - len(self.args) + 1))
        self.args[index] = item

    def __str__(self):
        return ','.join(str(arg) for arg in self.args if arg is not None)
