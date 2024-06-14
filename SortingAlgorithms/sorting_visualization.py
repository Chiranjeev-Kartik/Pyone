import matplotlib.animation as animation
import matplotlib.pyplot as plt
import random
import time
from sorting_algorithms import BubbleSort, InsertionSort, SelectionSort

random.seed(42)  # For Consistent nums


def bubble_sort(array):
    bs = BubbleSort(array)
    time.sleep(2)  # To let the user process the visuals initially :)
    while bs.bs_sort():
        yield bs.arr


def insertion_sort(array):
    ins = InsertionSort(array)
    time.sleep(2)
    for i in range(ins.length):
        yield ins.ins_sort(array, i)


def selection_sort(array):
    ss = SelectionSort(array)
    time.sleep(2)
    for i in range(ss.length):
        yield ss.ss_sort(array, i)


def animate_func(array, func, title):
    fig, ax = plt.subplots()
    bars = plt.bar(range(len(array)), array, color='b')
    plt.title(title, fontsize=16, fontweight='bold')  # Add title with large and bold text

    # Update function for animation
    def update(_array, _bars):
        for bar, val in zip(_bars, _array):
            bar.set_height(val)

    # Create animation
    _ = animation.FuncAnimation(fig, update, frames=func(array), fargs=(bars,), interval=100, repeat=False)

    # Show the plot
    plt.show()
    plt.close()


if __name__ == '__main__':
    nums = list(random.randint(1, 100) for _ in range(250))
    animate_func(nums, bubble_sort, "Bubble Sort Animation")
    nums = list(random.randint(1, 100) for _ in range(250))
    animate_func(nums, insertion_sort, "Insertion Sort Animation")
    nums = list(random.randint(1, 100) for _ in range(250))
    animate_func(nums, selection_sort, "Selection Sort Animation")
