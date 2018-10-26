class BinaryIndexedTree:
    def __init__(self, arr):
        self.bit_arr = [0] + arr
        for i in range(1, len(self.bit_arr)):
            j = i + (i & -i)
            if j < len(self.bit_arr):
                self.bit_arr[j] += self.bit_arr[i]

    def prefix_sum(self, i):
        i += 1
        result = 0
        while i > 0:
            result += self.bit_arr[i]
            i -= i & -i
        return result

    def update(self, i, val):
        i += 1
        diff = val - self.bit_arr[i]
        while i < len(self.bit_arr):
            self.bit_arr[i] += diff
            i += i & -i

    def range_sum(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)
