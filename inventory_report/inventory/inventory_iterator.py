from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.items = data
        self.idx = 0

    def __next__(self):
        try:
            item = self.items[self.idx]
        except IndexError:
            raise StopIteration()
        else:
            self.idx += 1
            return item
