class SelectionSort:
    def __init__(self, array):
        self.array = array
    def swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]
    def sort(self):
        for x in range(len(self.array)):
            for y in range(x + 1, len(self.array)):
                pass
    def compare(self, a, b):
        return a > b