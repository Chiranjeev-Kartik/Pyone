class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def bs_sort(self):
        swapped = False  # Main Logic ..................................................................................
        for i in range(self.length - 1):  # self.l - 1, as we are comparing with one element ahead.
            if self.arr[i] > self.arr[i + 1]:
                self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                swapped = True
        return swapped  # ..............................................................................................

    def sort(self):
        while self.bs_sort():  # Call bs_sort() until swapped variable returns False
            pass
        return self.arr


class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def qs_sort(self, _array):
        if len(_array) <= 1:
            return _array
        left, pivot, right = [], _array[-1], []
        # Main Logic ...................................................................................................
        left.extend([i for i in _array[:-1] if i < pivot])  # -1 for excluding pivot
        right.extend([i for i in _array[:-1] if i >= pivot])  # -1 for excluding pivot
        # ..............................................................................................................
        return self.qs_sort(left) + [pivot] + self.qs_sort(right)

    def sort(self):
        return self.qs_sort(self.arr)


class InsertionSort:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)

    @staticmethod
    def ins_sort(_array, idx):
        # Main Logic ...................................................................................................
        min_idx = min((i for i in range(idx) if _array[idx] < _array[i]), default=idx)  # Minimum index
        _array.insert(min_idx, _array.pop(idx))
        # ..............................................................................................................
        return _array

    def sort(self):
        for i in range(self.length):
            self.arr = self.ins_sort(self.arr, i)
        return self.arr


class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    @staticmethod
    def ms_sort(left, right):
        # Main Logic ...................................................................................................
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        merged.extend(left if left else right)
        return merged

    def sort(self, arr=None):
        arr = self.arr if arr is None else arr
        if len(arr) <= 1:
            return arr
        # Recursion logic ..............................................................................................
        left = self.sort(arr[:len(arr) // 2])
        right = self.sort(arr[len(arr) // 2:])
        return self.ms_sort(left, right)
    # ..................................................................................................................


class SelectionSort:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def ss_sort(self, _array, pos):
        # Main Logic ...................................................................................................
        min_idx = min(range(pos, self.length), key=_array.__getitem__)
        _array[pos], _array[min_idx] = _array[min_idx], _array[pos]
        # ..............................................................................................................
        return _array

    def sort(self):
        for i in range(len(self.arr)):
            self.arr = self.ss_sort(self.arr, i)
        return self.arr


# ........##.........##.........##.........##.........##.........##.........##.........##.........##.........##.......##


if __name__ == '__main__':
    import random
    import time

    def test_class(cls, _arrays):
        start = time.time()
        for arr in _arrays:
            if cls(arr).sort() != sorted(arr):
                print('FAIL', cls, arr)
                return 'FAIL', 0.0
        t_time = round((time.time() - start) / 60, 5)
        return 'OK', t_time

    random.seed(42)
    arrays = [random.choices(range(1, 1001), k=100) for _ in range(1000)]

    print(test_class(BubbleSort, arrays))
    print(test_class(QuickSort, arrays))
    print(test_class(InsertionSort, arrays))
    print(test_class(MergeSort, arrays))
    print(test_class(SelectionSort, arrays))
